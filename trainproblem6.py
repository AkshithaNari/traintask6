t_length=int(input("train length in m:"))
p_length=int(input("platform length in m:"))
total_length=t_length+p_length
t_pole=int(input("time taken to cross the pole in sec:"))
t_s=t_length/t_pole
t_t=p_length/t_s
t_p=total_length/t_t
print("time taken to cross platform in sec:",t_p)
