import pandas as pd
pd.options.mode.chained_assignment = None

def get_active_user(events, users):
    active_events = events[events.event_type=="engagement"]
    active_events['month'] = events.occurred_at.dt.month
    active_events['week'] = events.occurred_at.dt.week
    events_count = active_events.groupby(['month','week']).user_id.value_counts()
    last_engagement = active_events.groupby(['month','week','user_id']).occurred_at.max()

    active_user = pd.DataFrame({
        "events_count":events_count,
        "last_engagement":last_engagement
    })
    active_user = active_user.reset_index()
    active_user = pd.merge(active_user, users, on = "user_id")

    active_user['activate_length'] = pd.to_numeric((active_user.last_engagement - active_user.activated_at).dt.days)
    
    return active_user



def get_dropout_df(active_user):
    active_users_count = active_user.groupby('week').user_id.count()
    drop_out_count = []
    drop_out_rate = []
   
    
    for i in range(18,35):
        current_month_user = active_user.loc[(active_user.week==i),"user_id"]
        next_month_user = active_user.loc[(active_user.week== (i+1)),"user_id"]
        drop_out = len(list(set(current_month_user) - set(next_month_user)))
        drop_out_count.append(drop_out)
        drop_out_rate.append(drop_out/active_users_count[i])

    
    drop_out_df = pd.DataFrame({"active_user":active_users_count[:-1],
                            "drop_out_count":drop_out_count,
                            "drop_out_rate":drop_out_rate})
    
    drop_out_df = drop_out_df.reset_index()
    return drop_out_df

def get_newuser_df(active_user):
    active_users_count = active_user.groupby('week').user_id.count()
    new_user_count = []
    new_user_rate = [] 
    for i in range(19,36):
        current_month_user = active_user.loc[(active_user.week==i),"user_id"]
        last_month_user = active_user.loc[(active_user.week== (i-1)),"user_id"]
        new_user = len(list(set(current_month_user) - set(last_month_user)))
        new_user_count.append(new_user)
        new_user_rate.append(new_user/active_users_count[i])

    new_user_df = pd.DataFrame({"active_user":active_users_count[1:],
                            "new_user_count":new_user_count,
                            "new_user_rate":new_user_rate
    })
    
    new_user_df = new_user_df.reset_index()
    
    return new_user_df

def get_dropout_user_id(active_user, start, end):
    drop_out_id = set()
    for i in range(start,end):
        current_month_user = active_user.loc[(active_user.week==i),"user_id"]
        next_month_user = active_user.loc[(active_user.week== (i+1)),"user_id"]
        drop_out_id.update(((set(current_month_user) - set(next_month_user))))
    
    return drop_out_id


def get_dropout_events(events, drop_id, start, end):
    return events[(events.user_id.isin(drop_id)) & (events.occurred_at.dt.week.isin(range(start,end)))]