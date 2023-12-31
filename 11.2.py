def select_worst_captain(teams):
    worst_team=teams[-1]
    captain=worst_team[1]
    return captain
teams=[['Steven','Neena','Lex','Alexander','Bruce'],['David','Jack','Bill','Tom','Mike','Daniel'],['Alexander','Adam','Payam','Kevin','Sigal','Mike']]
worst_captain=select_worst_captain(teams)
print("Đội trưởng của đội tệ nhất là:",worst_captain)
        