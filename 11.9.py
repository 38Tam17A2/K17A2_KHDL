def party_late(arrivals,name):
    total_guests=len(arrivals)
    late_threshold=total_guests//2
    if name in arrivals:
        guests_index=arrivals.index(name)
        if guests_index<late_threshold and guests_index!=total_guests-1:
            return True
    return False
arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
guest_name='Gilbert'
print(party_late(arrivals,guest_name))
guest_name="Ford"
print(party_late(arrivals,guest_name))
guest_name="Mona"
print(party_late(arrivals,guest_name))