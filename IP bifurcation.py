user_input_address = input("Enter a IP range in /24 subnet:")
network_id = user_input_address.split('-')[0]
network_range = network_id.split('.')[0]+ '.' + network_id.split('.')[1]+'.' + network_id.split('.')[2]
ip_range_start = int(network_id.split('.')[3])
ip_range_end = int(user_input_address.split('-')[1])
