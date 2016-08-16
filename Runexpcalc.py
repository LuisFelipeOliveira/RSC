#coding: utf-8
import time #Importei para utilizar o Sleep, localizado ao final do código
import os #Importa comandos do SO
import sys #Importa o sistema
import ctypes #Serve para verificar, juntamente ao locale, as informações padrão do sistema
import locale # ^Acima^
#from pycolors import blue, red #Importa as cores, presentes em outro código
# Obs.: Red -> Errors / Blue -> Presentations 

#Não pude compilar dois .py juntos, para o import funcionar :/
blue = "\033[96m"
red = "\033[91m"

#Nota: aparentemente, o cx_Freeze não suporta cores do Python, que seriam exibidas no prompt de comando!



windll = ctypes.windll.kernel32
os_language = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

if os_language == "en_US":
	print(blue+"-> Loading content in English - US...\033[0;0m")
	while True:

		try: #Requisito para utilizar 'except'	
			skills = ["fm", "wc"]
			print(blue+'''
		-> Welcome to RuneScape Skill calculator! 
		-> Remember that we'll give you the most accurate results, but not counting with any bonuses.
		-> Made by Luis Felipe - TaylinG. :)\033[0;0m \n
			''')
			print("What's you nickname?\n")
			player_name = input("-> ")
			print("\n")
			print("What ability you need to calculate?\n")
			player_ability = input("-> ")
			if player_ability not in skills:	
				print(red+"Invalid ability.\033[0;0m \n")
				print("\n")
				print("Type 'restart' to reload the script or anything else to cancel. \n")
				return_to_start = input("->  ")
				if return_to_start == "restart":
					os.system("cls")
					continue
				else:
					print(blue+"\n Goodbye, %s!\033[0;0m"%(player_name))
					sys.exit()
					break
			else:
				if player_ability == "fm":
					os.system("cls")
					#Loading skill:
					print("Okay, %s, loading script for %s skill...\n"%(player_name, player_ability))
					#Player level in that skill:
					print("What's your level in %s?\n"%(player_ability))
					ability_level = int(input("-> "))
					print("\n")
					if ability_level < 1 or ability_level > 120:
						os.system("cls")
						print(red+'''
				!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				-> Your level must be more than 0 and less than 120. <-
				!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0;0m
						''')
						continue
					else:
						#Experience needed to player objective:
						print("How much experience you need to your objective?\n")
						xp_needed_to_objective = float(input("-> "))
						print("\n")
						#Logs used:
						print("Tip: Type 'other' to use values for an event, for example. Type 'see all' to see all log types!\n")
						print("What log do you intend to use?\n")
						log_type = input("-> ")
		
		
						#If using Maple Logs:
						if log_type == "maple":
							#Checking player level:
							if ability_level >= 45:
								print("You will receive at least 135xp per log.\n")
								maple_log_cost = 25 #price
								log_maple = 135 #exp
								log_maple_bonfire = 169 #exp
								total_logs_normal = xp_needed_to_objective / log_maple #using just for burn
								total_logs_bonfire = xp_needed_to_objective / log_maple_bonfire #using on bonfire
								total_xp_per_bag = log_maple + (log_maple_bonfire * 27) #xp/bag
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag #bags till reach objective
								time_till_objective = (bags_till_objective * 102) / 60 #time in minutes till reach objective -- the 102 value means one minute and 42 seconds (time to end a bag)
								time_in_hours = time_till_objective / 60 #time in hours till reach objective
								time_in_days = time_in_hours / 24 # time in days till reach objective
								money_spent = total_logs_normal * maple_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))	
							else:
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
			
		
						elif log_type == "magic":
							if ability_level >= 75:
								print("You'll receive at least 303.8xp per log.")
								magic_log_cost = 611
								log_magic = 303.8
								log_magic_bonfire = 308.5
								total_logs_normal = xp_needed_to_objective / log_magic
								total_logs_bonfire = xp_needed_to_objective / log_magic_bonfire
								total_xp_per_bag = log_magic + (log_magic_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * magic_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
			
			
						elif log_type == "blisterwood":
								if ability_level >= 76:
									print("You'll receive at least 303.8xp per log.")
									print("Please note that Blisterwood logs cannot be used in bonfire, and you can't buy them.")
									log_blisterwood = 303.8
									total_logs_normal = xp_needed_to_objective / log_blisterwood
									total_xp_per_bag = log_blisterwood * 28
									bags_till_objective = xp_needed_to_objective / total_xp_per_bag
									time_till_objective = (bags_till_objective * 102) / 60
									time_in_hours = time_till_objective / 60
									time_in_days = time_in_hours / 24
									print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
									print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))	
								else: 
									print("You don't have the necessary level to this log.")
									print("This application will end after 2 minutes, but if you want to, just close it and try again.")
			
		
						elif log_type == "elder":
							if ability_level >= 90:
								print("You'll receive at least 434.3xp per log.")
								elder_log_cost = 4893
								log_elder = 434.3
								log_elder_bonfire = 444.2
								total_logs_normal = xp_needed_to_objective / log_elder
								total_logs_bonfire = xp_needed_to_objective / log_elder_bonfire
								total_xp_per_bag = log_elder + (log_elder_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * elder_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
			
			
						elif log_type == "normal":
							if ability_level >= 1:
								print("You'll receive at least 40xp per log.")
								normal_log_cost = 94
								log_normal = 40
								log_normal_bonfire = 50
								total_logs_normal = xp_needed_to_objective / log_normal
								total_logs_bonfire = xp_needed_to_objective / log_normal_bonfire
								total_xp_per_bag = log_normal + (log_normal_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * normal_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
			
			
						elif log_type == "oak":
							if ability_level >= 15:
								print("You'll receive at least 60xp per log.")
								oak_log_cost = 77
								log_oak = 60
								log_oak_bonfire = 85
								total_logs_normal = xp_needed_to_objective / log_oak
								total_logs_bonfire = xp_needed_to_objective / log_oak_bonfire
								total_xp_per_bag = log_oak + (log_oak_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * oak_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")		
			
			
						elif log_type == "willow":
							if ability_level >= 30:
								print("You'll receive at least 90xp per log.")
								willow_log_cost = 23
								log_willow = 90
								log_willow_bonfire = 105
								total_logs_normal = xp_needed_to_objective / log_willow
								total_logs_bonfire = xp_needed_to_objective / log_willow_bonfire
								total_xp_per_bag = log_willow + (log_willow_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * willow_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
				
				
						elif log_type == "teak":
							if ability_level >= 35:
								print("You'll receive at least 105xp per log.")
								teak_log_cost = 81
								log_teak = 105
								log_teak_bonfire = 120
								total_logs_normal = xp_needed_to_objective / log_teak
								total_logs_bonfire = xp_needed_to_objective / log_teak_bonfire
								total_xp_per_bag = log_teak + (log_teak_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * teak_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
				
				
						elif log_type == "arctic pine":
							if ability_level >= 42:
								print("You'll receive at least 125xp per log.")
								arcticpine_log_cost = 77
								log_arcticpine = 125
								log_arcticpine_bonfire = 130
								total_logs_normal = xp_needed_to_objective / log_arcticpine
								total_logs_bonfire = xp_needed_to_objective / log_arcticpine_bonfire
								total_xp_per_bag = log_arcticpine + (log_arcticpine_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * arcticpine_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")				
				
				
						elif log_type == "mahogany":
							if ability_level >= 50:
								print("You'll receive at least 157.5xp per log.")
								mahogany_log_cost = 517
								log_mahogany = 157.5
								log_mahogany_bonfire = 180
								total_logs_normal = xp_needed_to_objective / log_mahogany
								total_logs_bonfire = xp_needed_to_objective / log_mahogany_bonfire
								total_xp_per_bag = log_mahogany + (log_mahogany_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * mahogany_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
				
			
						elif log_type == "eucalyptus":
							if ability_level >= 58:
								print("You'll receive at least 193.5xp per log.")
								eucalyptus_log_cost = 448
								log_eucalyptus = 193.5
								log_eucalyptus_bonfire = 195
								total_logs_normal = xp_needed_to_objective / log_eucalyptus
								total_logs_bonfire = xp_needed_to_objective / log_eucalyptus_bonfire
								total_xp_per_bag = log_eucalyptus + (log_eucalyptus_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * eucalyptus_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
					
				
						elif log_type == "yew":
							if ability_level >= 60:
								print("You'll receive at least 193.5xp per log.")
								yew_log_cost = 172
								log_yew = 202.5
								log_yew_bonfire = 260
								total_logs_normal = xp_needed_to_objective / log_yew
								total_logs_bonfire = xp_needed_to_objective / log_yew_bonfire
								total_xp_per_bag = log_yew + (log_yew_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * yew_log_cost
								print("So %s, you'll need %i %s logs to hit the objective."%(player_name, total_logs_normal, log_type))
								print("Tip: if you level up using bonfire, you'll need %i %s logs!"%(total_logs_bonfire, log_type))
								print("In total, you'll spent %i coins."%(money_spent))
								print("Using one log, and 27 in bonfire, you'll level up to your objective in about %i minutes, %i hours, or %f days."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just close it and try again.")
				
				
						elif log_type == "other":
							print("Okay, here we go!")
							xp_per_item = float(input("How much xp do you receive for each item or action?\n"))
							time_per_item = int(input("Please tell me in how much time do you receive that amount of xp (in seconds, of course xD).\n"))
							total_amount_exp_minute = xp_per_item * time_per_item
							total_amount_exp_hour = total_amount_exp_minute * 60
							total_amount_exp_day = total_amount_exp_hour * 24
							item_bag = input("It uses your bag?\n")
				
							if item_bag == "yes":
								spaces_bag = int(input("How many spaces?"))
								total_xp_use_bag = xp_per_item * spaces_bag
								time_per_bag = time_per_item * spaces_bag
								xp_bag_minute = total_xp_use_bag * time_per_bag
								xp_bag_hour = xp_bag_minute * 60
								xp_bag_day = xp_bag_hour * 24
								time_till_objective = xp_needed_to_objective / xp_bag_minute
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								print("So %s, you'll receive at least %i xp per minute, %i xp per hour and %i xp per day. And you'll reach your objective in %i minutes, %i hours, or %f days."%(player_name, xp_bag_minute, xp_bag_hour, xp_bag_day, time_till_objective, time_in_hours, time_in_days ))
					
					
							else:
								time_till_objective = xp_needed_to_objective / total_amount_exp_minute #time in minutes
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								print("So %s, you'll receive at least %i xp per minute, %i xp per hour and %i xp per day. And you'll reach your objective in %i minutes, %i hours, or %f days."%(player_name, total_amount_exp_minute, total_amount_exp_hour, total_amount_exp_day, time_till_objective, time_in_hours, time_in_days ))		
					
					
						elif log_type == "see all":
				
							#Normal log:
							normal_cost = 94
							normal_xp = 40
							number_normal = xp_needed_to_objective / normal_xp
							total_cost_normal = number_normal * normal_cost
							total_xp_normal = normal_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_normal
							time_till_objective = (bags_till_objective * 102) / 60
							time_normal = time_till_objective / 60
				
							#Oak log:
							oak_cost = 77
							oak_xp = 60
							number_oak = xp_needed_to_objective / oak_xp
							total_cost_oak = number_oak * oak_cost
							total_xp_oak = oak_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_oak
							time_till_objective = (bags_till_objective * 102) / 60
							time_oak = time_till_objective / 60
					
							#Willow log:
							willow_cost = 23
							willow_xp = 90
							number_willow = xp_needed_to_objective / willow_xp
							total_cost_willow =	 number_willow * willow_cost
							total_xp_willow = willow_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_willow
							time_till_objective = (bags_till_objective * 102) / 60
							time_willow = time_till_objective / 60
				
							#Teak log:
							teak_cost = 81
							teak_xp = 105
							number_teak = xp_needed_to_objective / teak_xp
							total_cost_teak = number_teak * teak_cost
							total_xp_teak = teak_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_teak
							time_till_objective = (bags_till_objective * 102) / 60
							time_teak = time_till_objective / 60
				
							#Arctic Pine log:
							arctic_pine_cost = 77
							arctic_pine_xp = 125
							number_arctic_pine = xp_needed_to_objective / arctic_pine_xp
							total_cost_arctic_pine = number_arctic_pine * arctic_pine_cost
							total_xp_arctic_pine = arctic_pine_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_arctic_pine
							time_till_objective = (bags_till_objective * 102) / 60
							time_arctic_pine = time_till_objective / 60
				
							#Maple log:
							maple_cost = 25
							maple_xp = 135
							number_maple = xp_needed_to_objective / maple_xp
							total_cost_maple =	number_maple * maple_cost
							total_xp_maple = maple_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_maple
							time_till_objective = (bags_till_objective * 102) / 60
							time_maple = time_till_objective / 60
				
							#Mahogany log:
							mahogany_cost = 517
							mahogany_xp = 157.5
							number_mahogany = xp_needed_to_objective / mahogany_xp
							total_cost_mahogany = number_mahogany * mahogany_cost
							total_xp_mahogany = mahogany_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_mahogany
							time_till_objective = (bags_till_objective * 102) / 60
							time_mahogany = time_till_objective / 60
				
							#Eucalyptus log:
							eucalyptus_cost = 448
							eucalyptus_xp = 193.5
							number_eucalyptus = xp_needed_to_objective / eucalyptus_xp
							total_cost_eucalyptus =	number_eucalyptus * eucalyptus_cost
							total_xp_eucalyptus = eucalyptus_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_eucalyptus
							time_till_objective = (bags_till_objective * 102) / 60
							time_eucalyptus = time_till_objective / 60
				
							#Yew log:
							yew_cost = 172
							yew_xp = 202.5
							number_yew = xp_needed_to_objective / yew_xp
							total_cost_yew = number_yew * yew_cost
							total_xp_yew = yew_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_yew
							time_till_objective = (bags_till_objective * 102) / 60
							time_yew = time_till_objective / 60		
				
							#Magic log:
							magic_cost = 611
							magic_xp = 303.8
							number_magic = xp_needed_to_objective / magic_xp
							total_cost_magic = number_magic * magic_cost
							total_xp_magic = magic_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_magic
							time_till_objective = (bags_till_objective * 102) / 60
							time_magic = time_till_objective / 60
				
							#Blisterwood log:
							blisterwood_cost = "You can't buy them."
							blisterwood_xp = 303.8
							number_blisterwood = xp_needed_to_objective / blisterwood_xp
							total_xp_blisterwood = blisterwood_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_blisterwood
							time_till_objective = (bags_till_objective * 102) / 60
							time_blisterwood = time_till_objective / 60		
				
							#Elder log:
							elder_cost = 4893
							elder_xp = 434.3
							number_elder = xp_needed_to_objective / elder_xp
							total_cost_elder = number_elder * elder_cost
							total_xp_elder = elder_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_elder
							time_till_objective = (bags_till_objective * 102) / 60
							time_elder = time_till_objective / 60
				
							print('''
			   -Normal: 
				-> Level required: 1
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours
				
			   -Oak: 
				-> Level required: 15
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours
				
			   -Willow: 
				-> Level required: 30
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Teak: 
				-> Level required: 35
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Arctic Pine: 
				-> Level required: 42
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Maple: 
				-> Level required: 45
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Mahogany: 
				-> Level required: 50
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Eucalyptus: 
				-> Level required: 58
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Yew: 
				-> Level required: 60
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Magic: 
				-> Level required: 75
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours

			   -Blisterwood: 
				-> Level required: 76
				-> Number of logs: %i
				-> Total cost: %s 
				-> Time untill reach objective:  %i hours	
				
			   -Elder: 
				-> Level required: 90
				-> Number of logs: %i
				-> Total cost: %i coins
				-> Time untill reach objective:  %i hours
				
					'''%(number_normal, total_cost_normal, time_normal, number_oak, total_cost_oak, time_oak, number_willow, total_cost_willow, time_willow, number_teak, total_cost_teak, time_teak, number_arctic_pine, total_cost_arctic_pine, time_arctic_pine, number_maple, total_cost_maple, time_maple, number_mahogany, total_cost_mahogany, time_mahogany, number_eucalyptus, total_cost_eucalyptus, time_eucalyptus, number_yew, total_cost_yew, time_yew, number_magic, total_cost_magic, time_magic, number_blisterwood, blisterwood_cost, time_blisterwood, number_elder, total_cost_elder, time_elder))


						return_to_start = input("Do you want to reload the script? Type 'yes' or 'no'. \n")
						if return_to_start == "yes":
							os.system("cls") #Limpa o prompt de comando e, nesse caso, funciona apenas em sistemas operacionais Windows
							continue #Vai informar que o While pode ser carregado, recarregando assim TODO o código dentro do mesmo
						elif return_to_start == "no":
							print("Application will close in 2 minutes. But if you want to, just close it manually.")
							close_App = input("Type 'close' to end the application.\n")
							if close_App == "close":
								sys.exit()
							break #Vai informar que o While NÃO deve ser carregado, logo, a aplicação apenas prossegue para seus 2 minutos de vida pós-processamento
					
			
				elif player_ability == "wc":
					os.system("cls")
					#Loading skill:
					print("Okay, %s, loading script for %s skill...\n"%(player_name, player_ability))
					#Player level in that ability:
					ability_level = int(input("What's your level in %s?\n"%(player_ability)))
					if ability_level < 1 or ability_level > 120:
						os.system("cls")
						print(red+'''
					!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
					-> Your level must be more than 0 and less than 120. <-
					!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0;0m
						''')
						continue
					else:
						#Experience needed to player goal:
						xp_needed_to_objective = float(input("How much experience you need to your objective?\n"))
						#Type of tree to chop down:
						tree_type = input("What tree do you intend to chop down? \n")
				
						#Code for normal tree:
						if tree_type == "normal":
							if ability_level >= 1:
								print("You'll receive at least 25xp for log.")
								xp_normal = 25
								price_for_sell = 94
								qtd_logs_needed = xp_needed_to_objective / xp_normal
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
						
						elif tree_type == "oak":
							if ability_level >= 15:
								print("You'll receive at least 37.5xp for log.")
								xp_oak = 37.5
								price_for_sell = 76
								qtd_logs_needed = xp_needed_to_objective / xp_oak
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
						
						elif tree_type == "willow":
							if ability_level >= 30:
								print("You'll receive at least 67.5xp for log.")
								xp_willow = 67.5
								price_for_sell = 22
								qtd_logs_needed = xp_needed_to_objective / xp_willow
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
					
						elif tree_type == "teak":
							if ability_level >= 35:
								print("You'll receive at least 85xp for log.")
								xp_teak = 85
								price_for_sell = 98
								qtd_logs_needed = xp_needed_to_objective / xp_teak
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
						
					
						elif tree_type == "maple":
							if ability_level >= 45:
								print("You'll receive at least 100xp for log.")
								xp_maple = 100
								price_for_sell = 25
								qtd_logs_needed = xp_needed_to_objective / xp_maple
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
						
							
						elif tree_type == "mahogany":
							if ability_level >= 50:
								print("You'll receive at least 125xp for log.")
								xp_mahogany = 125
								price_for_sell = 489
								qtd_logs_needed = xp_needed_to_objective / xp_mahogany
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
					
						elif tree_type == "arctic pine":
							if ability_level >= 54:
								print("You'll receive at least 140.2xp for log.")
								xp_arctic_pine = 140.2
								price_for_sell = 71
								qtd_logs_needed = xp_needed_to_objective / xp_arctic_pine
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
						
					
						elif tree_type == "eucalyptus":
							if ability_level >= 58:
								print("You'll receive at least 165xp for log.")
								xp_eucalyptus = 165
								price_for_sell = 460
								qtd_logs_needed = xp_needed_to_objective / xp_eucalyptus
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
							
						elif tree_type == "yew":
							if ability_level >= 60:
								print("You'll receive at least 175xp for log.")
								xp_yew = 175
								price_for_sell = 169
								qtd_logs_needed = xp_needed_to_objective / xp_yew
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
							
						elif tree_type == "ivy":
							if ability_level >= 68:
								print("You'll receive at least 332.5xp.")
								xp_ivy = 332.5
								price_for_sell = "Ivy don't give logs."
								qtd_logs_needed = xp_needed_to_objective / xp_ivy
								total_profit = price_for_sell
								print("So, %s, you'll need to chop down %s %i times."%(player_name, tree_type, qtd_logs_needed))
								print("Total profit: %s"%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
						
						elif tree_type == "magic":
							if ability_level >= 75:
								print("You'll receive at least 250xp for log.")
								xp_magic = 250
								price_for_sell = 613
								qtd_logs_needed = xp_needed_to_objective / xp_magic
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
						
						elif tree_type == "blisterwood":
							if ability_level >= 76:
								print("You'll receive at least 200xp for log.")
								xp_blisterwood = 200
								price_for_sell = "You can't sell blisterwood logs."
								qtd_logs_needed = xp_needed_to_objective / xp_blisterwood
								total_profit = price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %s"%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
						
						elif tree_type == "cursed magic":
							if ability_level >= 82:
								print("You'll receive at least 275xp for log.")
								xp_cursed_magic = 275
								price_for_sell = "It's a special kind of magic tree, found in wilderness after finished the quest. Can't sell cursed logs, 'cause they turn to normal."
								qtd_logs_needed = xp_needed_to_objective / xp_cursed_magic
								total_profit = price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %s"%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
							
						elif tree_type == "mutated vine":
							if ability_level >= 83:
								print("You'll receive at least 140xp for log.")
								xp_mutated_vine = 140
								price_for_sell = "Can't sell."
								qtd_logs_needed = xp_needed_to_objective / xp_mutated_vine
								total_profit = price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %s"%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
							
						elif tree_type == "curly root" or tree_type == "straight root":
							if ability_level >= 83:
								print("You'll receive at least 161.6xp for log.")
								xp_roots = 161.6
								price_for_sell = "Can't sell."
								qtd_logs_needed = xp_needed_to_objective / xp_roots
								total_profit = price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %s"%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
					
						elif tree_type == "elder":
							if ability_level >= 90:
								print("You'll receive at least 325xp for log.")
								xp_elder = 325
								price_for_sell = 4896
								qtd_logs_needed = xp_needed_to_objective / xp_elder
								total_profit = qtd_logs_needed * price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %i coins."%(total_profit))	
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
							
						
						elif tree_type == "crystal":
							if ability_level >= 94:
								print("You'll receive at least 434.5xp for log.")
								xp_crystal = 434.5
								price_for_sell = "Crystal trees don't give any logs."
								qtd_logs_needed = xp_needed_to_objective / xp_crystal
								total_profit = price_for_sell
								print("So, %s, you'll need to chop down %i %s trees."%(player_name, qtd_logs_needed, tree_type))
								print("Total profit: %s"%(total_profit))	
						
							else: 
								print("You don't have the necessary level to this log.")
								print("This application will end after 2 minutes, but if you want to, just reinitiate.")
						
						
						return_to_start = input("Do you want to reload the script? Type 'yes' or 'no'. \n")
						if return_to_start == "yes":
							os.system("cls") #Limpa o prompt de comando e, nesse caso, funciona apenas em sistemas operacionais Windows
							continue #Vai informar que o While pode ser carregado, recarregando assim TODO o código dentro do mesmo
						elif return_to_start == "no":
							print("Application will close in 2 minutes. But if you want to, just close it manually.")
							close_App = input("Type 'close' to end the application.\n")
							if close_App == "close":
								sys.exit()
							break #Vai informar que o While NÃO deve ser carregado, logo, a aplicação apenas prossegue para seus 2 minutos de vida pós-processamento
							
		except ValueError: #Nesse caso, quando o erro ValueError for disparado, ele fará isso:
			print(red+"Invalid value.\033[0;0m")
			print("Type 'restart' to reload the script or anything else to cancel. \n")
			return_to_start = input("->  ")
			if return_to_start == "restart":
				os.system("cls")
				continue
			else:
				print(blue+"\n Goodbye, %s!\033[0;0m"%(player_name))
				sys.exit()
				break


elif os_language == "pt_BR":
	print(blue+"-> Carregando conteúdo em Português - BR...\033[0;0m")
	while True:

		try: #Requisito para utilizar 'except'	
			skills = ["arte do fogo", "corte de lenha"]
			print(blue+'''
		-> Bem-vindo ao RuneScape Skill calculator! 
		-> Lembre-se de que nós daremos os resultados mais precisos, mas sem contar com bônus.
		-> Feito por Luis Felipe - TaylinG. :)\033[0;0m \n
			''')
			print("Qual é o seu nome?\n")
			player_name = input("-> ")
			print("\n")
			print("Qual habilidade você gostaria de calcular?\n")
			player_ability = input("-> ")
			if player_ability not in skills:	
				print(red+"Habilidade inválida.\033[0;0m \n")
				print("\n")
				print("Digite 'recomeçar' para recarregar o código ou qualquer tecla para finalizar. \n")
				return_to_start = input("->  ")
				if return_to_start == "recomeçar":
					os.system("cls")
					continue
				else:
					print(blue+"\n Até mais, %s!\033[0;0m"%(player_name))
					sys.exit()
					break
			else:
				if player_ability == "arte do fogo":
					os.system("cls")
					#Loading skill:
					print("Certo, %s, carregando script para a habilidade %s ...\n"%(player_name, player_ability))
					#Player level in that skill:
					print("Qual é o seu nível em %s?\n"%(player_ability))
					ability_level = int(input("-> "))
					print("\n")
					if ability_level < 1 or ability_level > 120:
						os.system("cls")
						print(red+'''
				!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				-> Seu nível deve ser maior que 0 e menor que 120. <-
				!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0;0m
						''')
						continue
					else:
						#Experience needed to player objective:
						print("Qual a quantidade necessária de experiência para atingir seu objetivo?\n")
						xp_needed_to_objective = float(input("-> "))
						print("\n")
						#Logs used:
						print("Dica: digite 'outro' para utilizar valores personalizados, para um evento, por exemplo. Digite 'ver todos' para ver todas as informações para todos os tipos de lenha!\n")
						print("Que tipo de lenha você pretende utilizar?\n")
						log_type = input("-> ")
		
		
						#If using Maple Logs:
						if log_type == "bordo":
							#Checking player level:
							if ability_level >= 45:
								print("Você receberá pelo menos 135xp por lenha.\n")
								maple_log_cost = 25 #price
								log_maple = 135 #exp
								log_maple_bonfire = 169 #exp
								total_logs_normal = xp_needed_to_objective / log_maple #using just for burn
								total_logs_bonfire = xp_needed_to_objective / log_maple_bonfire #using on bonfire
								total_xp_per_bag = log_maple + (log_maple_bonfire * 27) #xp/bag
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag #bags till reach objective
								time_till_objective = (bags_till_objective * 102) / 60 #time in minutes till reach objective -- the 102 value means one minute and 42 seconds (time to end a bag)
								time_in_hours = time_till_objective / 60 #time in hours till reach objective
								time_in_days = time_in_hours / 24 # time in days till reach objective
								money_spent = total_logs_normal * maple_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))	
							else:
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
			
		
						elif log_type == "mágica":
							if ability_level >= 75:
								print("Você receberá pelo menos 303.8xp por lenha.\n")
								magic_log_cost = 611
								log_magic = 303.8
								log_magic_bonfire = 308.5
								total_logs_normal = xp_needed_to_objective / log_magic
								total_logs_bonfire = xp_needed_to_objective / log_magic_bonfire
								total_xp_per_bag = log_magic + (log_magic_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * magic_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("\n")
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("\n")
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("\n")
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
			
			
						elif log_type == "inflamadeira":
								if ability_level >= 76:
									print("Você receberá pelo menos 303.8xp por lenha.\n")
									print("Note que lenhas de inflamadeira não podem ser utilizadas em fogueiras, e você não pode comprá-las.")
									log_blisterwood = 303.8
									total_logs_normal = xp_needed_to_objective / log_blisterwood
									total_xp_per_bag = log_blisterwood * 28
									bags_till_objective = xp_needed_to_objective / total_xp_per_bag
									time_till_objective = (bags_till_objective * 102) / 60
									time_in_hours = time_till_objective / 60
									time_in_days = time_in_hours / 24
									print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
									print("\n")
									print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))	
								else: 
									print("\n")
									print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
									print("\n")
									print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
			
		
						elif log_type == "anciã":
							if ability_level >= 90:
								print("Você receberá pelo menos 434.3xp por lenha.\n")
								elder_log_cost = 4893
								log_elder = 434.3
								log_elder_bonfire = 444.2
								total_logs_normal = xp_needed_to_objective / log_elder
								total_logs_bonfire = xp_needed_to_objective / log_elder_bonfire
								total_xp_per_bag = log_elder + (log_elder_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * elder_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
			
			
						elif log_type == "normal":
							if ability_level >= 1:
								print("Você receberá pelo menos 40xp por lenha.\n")
								normal_log_cost = 94
								log_normal = 40
								log_normal_bonfire = 50
								total_logs_normal = xp_needed_to_objective / log_normal
								total_logs_bonfire = xp_needed_to_objective / log_normal_bonfire
								total_xp_per_bag = log_normal + (log_normal_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * normal_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
			
			
						elif log_type == "carvalho":
							if ability_level >= 15:
								print("Você receberá pelo menos 60xp por lenha.\n")
								oak_log_cost = 77
								log_oak = 60
								log_oak_bonfire = 85
								total_logs_normal = xp_needed_to_objective / log_oak
								total_logs_bonfire = xp_needed_to_objective / log_oak_bonfire
								total_xp_per_bag = log_oak + (log_oak_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * oak_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
			
			
						elif log_type == "salgueiro":
							if ability_level >= 30:
								print("Você receberá pelo menos 90xp por lenha.\n")
								willow_log_cost = 23
								log_willow = 90
								log_willow_bonfire = 105
								total_logs_normal = xp_needed_to_objective / log_willow
								total_logs_bonfire = xp_needed_to_objective / log_willow_bonfire
								total_xp_per_bag = log_willow + (log_willow_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * willow_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
				
				
						elif log_type == "teca":
							if ability_level >= 35:
								print("Você receberá pelo menos 105xp por lenha.\n")
								teak_log_cost = 81
								log_teak = 105
								log_teak_bonfire = 120
								total_logs_normal = xp_needed_to_objective / log_teak
								total_logs_bonfire = xp_needed_to_objective / log_teak_bonfire
								total_xp_per_bag = log_teak + (log_teak_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * teak_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
				
				
						elif log_type == "pinheiro do ártico":
							if ability_level >= 42:
								print("Você receberá pelo menos 125xp por lenha.\n")
								arcticpine_log_cost = 77
								log_arcticpine = 125
								log_arcticpine_bonfire = 130
								total_logs_normal = xp_needed_to_objective / log_arcticpine
								total_logs_bonfire = xp_needed_to_objective / log_arcticpine_bonfire
								total_xp_per_bag = log_arcticpine + (log_arcticpine_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * arcticpine_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")				
				
				
						elif log_type == "mogno":
							if ability_level >= 50:
								print("Você receberá pelo menos 157.5xp por lenha.\n")
								mahogany_log_cost = 517
								log_mahogany = 157.5
								log_mahogany_bonfire = 180
								total_logs_normal = xp_needed_to_objective / log_mahogany
								total_logs_bonfire = xp_needed_to_objective / log_mahogany_bonfire
								total_xp_per_bag = log_mahogany + (log_mahogany_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * mahogany_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
				
			
						elif log_type == "eucalipto":
							if ability_level >= 58:
								print("Você receberá pelo menos 193.5xp por lenha.\n")
								eucalyptus_log_cost = 448
								log_eucalyptus = 193.5
								log_eucalyptus_bonfire = 195
								total_logs_normal = xp_needed_to_objective / log_eucalyptus
								total_logs_bonfire = xp_needed_to_objective / log_eucalyptus_bonfire
								total_xp_per_bag = log_eucalyptus + (log_eucalyptus_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * eucalyptus_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))	
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
					
				
						elif log_type == "teixo":
							if ability_level >= 60:
								print("Você receberá pelo menos 193.5xp por lenha.\n")
								yew_log_cost = 172
								log_yew = 202.5
								log_yew_bonfire = 260
								total_logs_normal = xp_needed_to_objective / log_yew
								total_logs_bonfire = xp_needed_to_objective / log_yew_bonfire
								total_xp_per_bag = log_yew + (log_yew_bonfire * 27)
								bags_till_objective = xp_needed_to_objective / total_xp_per_bag
								time_till_objective = (bags_till_objective * 102) / 60
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								money_spent = total_logs_normal * yew_log_cost
								print("Então %s, você necessita de %i lenhas de %s para atingir o objetivo."%(player_name, total_logs_normal, log_type))
								print("Dica: se você upar utilizando a lenha na fogueira, precisará apenas de %i lenhas de %s!"%(total_logs_bonfire, log_type))
								print("No total, você irá gastar %i moedas."%(money_spent))
								print("Acendendo uma lenha, e utilizando o restante na fogueira, você irá atingir seu objetivo em %i minutos, %i horas, ou %f dias."%(time_till_objective, time_in_hours, time_in_days))
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
				
				
						elif log_type == "outro":
							print("Ok, vamos lá!\n")
							print("Qual a quantidade de experiência que você recebe por item ou ação?\n")
							xp_per_item = float(input("-> "))
							print("Por favor, me informe de quanto em quanto tempo você recebe essa quantidade de experiência (em segundos, claro xD).\n")
							time_per_item = int(input("-> "))
							total_amount_exp_minute = xp_per_item * time_per_item
							total_amount_exp_hour = total_amount_exp_minute * 60
							total_amount_exp_day = total_amount_exp_hour * 24
							print("Utiliza espaços na mochila?\n")
							item_bag = input("-> ")
				
							if item_bag == "sim":
								print("Quantos espaços, no total?\n")
								spaces_bag = int(input("-> "))
								total_xp_use_bag = xp_per_item * spaces_bag
								time_per_bag = time_per_item * spaces_bag
								xp_bag_minute = total_xp_use_bag * time_per_bag
								xp_bag_hour = xp_bag_minute * 60
								xp_bag_day = xp_bag_hour * 24
								time_till_objective = xp_needed_to_objective / xp_bag_minute
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								print("Então %s, você receberá %i xp por minuto, %i xp por hora e %i xp por dia. Você atingirá seu objetivo em %i minutos, %i horas, ou %f dias."%(player_name, xp_bag_minute, xp_bag_hour, xp_bag_day, time_till_objective, time_in_hours, time_in_days ))
					
					
							else:
								time_till_objective = xp_needed_to_objective / total_amount_exp_minute #time in minutes
								time_in_hours = time_till_objective / 60
								time_in_days = time_in_hours / 24
								print("Então %s, você receberá %i xp por minuto, %i xp por hora e %i xp por dia. Você atingirá seu objetivo em %i minutos, %i horas, ou %f dias."%(player_name, total_amount_exp_minute, total_amount_exp_hour, total_amount_exp_day, time_till_objective, time_in_hours, time_in_days ))		
					
					
						elif log_type == "ver todos":
				
							#Normal log:
							normal_cost = 94
							normal_xp = 40
							number_normal = xp_needed_to_objective / normal_xp
							total_cost_normal = number_normal * normal_cost
							total_xp_normal = normal_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_normal
							time_till_objective = (bags_till_objective * 102) / 60
							time_normal = time_till_objective / 60
				
							#Oak log:
							oak_cost = 77
							oak_xp = 60
							number_oak = xp_needed_to_objective / oak_xp
							total_cost_oak = number_oak * oak_cost
							total_xp_oak = oak_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_oak
							time_till_objective = (bags_till_objective * 102) / 60
							time_oak = time_till_objective / 60
					
							#Willow log:
							willow_cost = 23
							willow_xp = 90
							number_willow = xp_needed_to_objective / willow_xp
							total_cost_willow =	 number_willow * willow_cost
							total_xp_willow = willow_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_willow
							time_till_objective = (bags_till_objective * 102) / 60
							time_willow = time_till_objective / 60
				
							#Teak log:
							teak_cost = 81
							teak_xp = 105
							number_teak = xp_needed_to_objective / teak_xp
							total_cost_teak = number_teak * teak_cost
							total_xp_teak = teak_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_teak
							time_till_objective = (bags_till_objective * 102) / 60
							time_teak = time_till_objective / 60
				
							#Arctic Pine log:
							arctic_pine_cost = 77
							arctic_pine_xp = 125
							number_arctic_pine = xp_needed_to_objective / arctic_pine_xp
							total_cost_arctic_pine = number_arctic_pine * arctic_pine_cost
							total_xp_arctic_pine = arctic_pine_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_arctic_pine
							time_till_objective = (bags_till_objective * 102) / 60
							time_arctic_pine = time_till_objective / 60
				
							#Maple log:
							maple_cost = 25
							maple_xp = 135
							number_maple = xp_needed_to_objective / maple_xp
							total_cost_maple =	number_maple * maple_cost
							total_xp_maple = maple_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_maple
							time_till_objective = (bags_till_objective * 102) / 60
							time_maple = time_till_objective / 60
				
							#Mahogany log:
							mahogany_cost = 517
							mahogany_xp = 157.5
							number_mahogany = xp_needed_to_objective / mahogany_xp
							total_cost_mahogany = number_mahogany * mahogany_cost
							total_xp_mahogany = mahogany_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_mahogany
							time_till_objective = (bags_till_objective * 102) / 60
							time_mahogany = time_till_objective / 60
				
							#Eucalyptus log:
							eucalyptus_cost = 448
							eucalyptus_xp = 193.5
							number_eucalyptus = xp_needed_to_objective / eucalyptus_xp
							total_cost_eucalyptus =	number_eucalyptus * eucalyptus_cost
							total_xp_eucalyptus = eucalyptus_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_eucalyptus
							time_till_objective = (bags_till_objective * 102) / 60
							time_eucalyptus = time_till_objective / 60
				
							#Yew log:
							yew_cost = 172
							yew_xp = 202.5
							number_yew = xp_needed_to_objective / yew_xp
							total_cost_yew = number_yew * yew_cost
							total_xp_yew = yew_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_yew
							time_till_objective = (bags_till_objective * 102) / 60
							time_yew = time_till_objective / 60		
				
							#Magic log:
							magic_cost = 611
							magic_xp = 303.8
							number_magic = xp_needed_to_objective / magic_xp
							total_cost_magic = number_magic * magic_cost
							total_xp_magic = magic_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_magic
							time_till_objective = (bags_till_objective * 102) / 60
							time_magic = time_till_objective / 60
				
							#Blisterwood log:
							blisterwood_cost = "Não é possível comprar."
							blisterwood_xp = 303.8
							number_blisterwood = xp_needed_to_objective / blisterwood_xp
							total_xp_blisterwood = blisterwood_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_blisterwood
							time_till_objective = (bags_till_objective * 102) / 60
							time_blisterwood = time_till_objective / 60		
				
							#Elder log:
							elder_cost = 4893
							elder_xp = 434.3
							number_elder = xp_needed_to_objective / elder_xp
							total_cost_elder = number_elder * elder_cost
							total_xp_elder = elder_xp * 28
							bags_till_objective = xp_needed_to_objective / total_xp_elder
							time_till_objective = (bags_till_objective * 102) / 60
							time_elder = time_till_objective / 60
				
							print('''
			   -Normal: 
				-> Nível requerido: 1
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas
				
			   -Carvalho: 
				-> Nível requerido: 15
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas
				
			   -Salgueiro: 
				-> Nível requerido: 30
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas
				
			   -Teca: 
				-> Nível requerido: 35
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas

			   -Pinheiro do ártico: 
				-> Nível requerido: 42
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas

			   -Bordo: 
				-> Nível requerido: 45
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas

			   -Mogno: 
				-> Nível requerido: 50
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas

			   -Eucalipto: 
				-> Nível requerido: 58
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas

			   -Teixo: 
				-> Nível requerido: 60
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas

			   -Mágica: 
				-> Nível requerido: 75
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas

			   -Inflamadeira: 
				-> Nível requerido: 76
				-> Número de lenhas: %i
				-> Custo total: %s 
				-> Tempo até atingir o objetivo:  %i horas	
				
			   -Anciã: 
				-> Nível requerido: 90
				-> Número de lenhas: %i
				-> Custo total: %i moedas
				-> Tempo até atingir o objetivo:  %i horas
				
					'''%(number_normal, total_cost_normal, time_normal, number_oak, total_cost_oak, time_oak, number_willow, total_cost_willow, time_willow, number_teak, total_cost_teak, time_teak, number_arctic_pine, total_cost_arctic_pine, time_arctic_pine, number_maple, total_cost_maple, time_maple, number_mahogany, total_cost_mahogany, time_mahogany, number_eucalyptus, total_cost_eucalyptus, time_eucalyptus, number_yew, total_cost_yew, time_yew, number_magic, total_cost_magic, time_magic, number_blisterwood, blisterwood_cost, time_blisterwood, number_elder, total_cost_elder, time_elder))

						
						print("Você gostaria de reiniciar o código? Digite 'sim' ou 'não'. \n")
						return_to_start = input("-> ")
						if return_to_start == "sim":
							os.system("cls") #Limpa o prompt de comando e, nesse caso, funciona apenas em sistemas operacionais Windows
							continue #Vai informar que o While pode ser carregado, recarregando assim TODO o código dentro do mesmo
						elif return_to_start == "não":
							print("A aplicação irá fechar em 2 minutos. Se desejar, feche manualmente.")
							print("Digite 'fechar' para finalizar a aplicação.\n")
							close_App = input("-> ")
							if close_App == "fechar":
								sys.exit()
							break #Vai informar que o While NÃO deve ser carregado, logo, a aplicação apenas prossegue para seus 2 minutos de vida pós-processamento
					
			
				elif player_ability == "corte de lenha":
					os.system("cls")
					#Loading skill:
					print("Certo, %s, carregando script para a habilidade %s...\n"%(player_name, player_ability))
					#Player level in that ability:
					print("Qual é o seu nível em %s?\n"%(player_ability))
					ability_level = int(input("-> "))
					print("\n")
					if ability_level < 1 or ability_level > 120:
						os.system("cls")
						print(red+'''
					!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
					-> Seu nível deve ser maior que 0 e menor que 120. <-
					!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0;0m
						''')
						continue
					else:
						#Experience needed to player goal:
						print("Qual a quantidade necessária de experiência para atingir seu objetivo?\n")
						xp_needed_to_objective = float(input("-> "))
						print("\n")
						#Type of tree to chop down:
						print("Que tipo de árvore você pretende cortar? \n")
						tree_type = input("-> ")
				
						#Code for normal tree:
						if tree_type == "normal":
							if ability_level >= 1:
								print("Você receberá pelo menos 25xp por lenha.\n")
								xp_normal = 25
								price_for_sell = 94
								qtd_logs_needed = xp_needed_to_objective / xp_normal
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
						
						elif tree_type == "carvalho":
							if ability_level >= 15:
								print("Você receberá pelo menos 37.5xp por lenha.\n")
								xp_oak = 37.5
								price_for_sell = 76
								qtd_logs_needed = xp_needed_to_objective / xp_oak
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
						
						elif tree_type == "salgueiro":
							if ability_level >= 30:
								print("Você receberá pelo menos 67.5xp por lenha.\n")
								xp_willow = 67.5
								price_for_sell = 22
								qtd_logs_needed = xp_needed_to_objective / xp_willow
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
					
						elif tree_type == "teca":
							if ability_level >= 35:
								print("Você receberá pelo menos 85xp por lenha.\n")
								xp_teak = 85
								price_for_sell = 98
								qtd_logs_needed = xp_needed_to_objective / xp_teak
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
						
					
						elif tree_type == "bordo":
							if ability_level >= 45:
								print("Você receberá pelo menos 100xp por lenha.\n")
								xp_maple = 100
								price_for_sell = 25
								qtd_logs_needed = xp_needed_to_objective / xp_maple
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
						
							
						elif tree_type == "mogno":
							if ability_level >= 50:
								print("Você receberá pelo menos 125xp por lenha.\n")
								xp_mahogany = 125
								price_for_sell = 489
								qtd_logs_needed = xp_needed_to_objective / xp_mahogany
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
					
						elif tree_type == "pinheiro do ártico":
							if ability_level >= 54:
								print("Você receberá pelo menos 140.2xp por lenha.\n")
								xp_arctic_pine = 140.2
								price_for_sell = 71
								qtd_logs_needed = xp_needed_to_objective / xp_arctic_pine
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
						
					
						elif tree_type == "eucalipto":
							if ability_level >= 58:
								print("Você receberá pelo menos 165xp por lenha.\n")
								xp_eucalyptus = 165
								price_for_sell = 460
								qtd_logs_needed = xp_needed_to_objective / xp_eucalyptus
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
							
						elif tree_type == "teixo":
							if ability_level >= 60:
								print("Você receberá pelo menos 175xp por lenha.\n")
								xp_yew = 175
								price_for_sell = 169
								qtd_logs_needed = xp_needed_to_objective / xp_yew
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
							
						elif tree_type == "hera":
							if ability_level >= 68:
								print("Você receberá pelo menos 332.5xp.\n")
								xp_ivy = 332.5
								price_for_sell = "Heras não fornecem lenha."
								qtd_logs_needed = xp_needed_to_objective / xp_ivy
								total_profit = price_for_sell
								print("Então, %s, você deverá cortar %s %i vezes."%(player_name, tree_type, qtd_logs_needed))
								print("Lucro total: %s"%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
						
						elif tree_type == "mágica":
							if ability_level >= 75:
								print("Você receberá pelo menos 250xp por lenha.\n")
								xp_magic = 250
								price_for_sell = 613
								qtd_logs_needed = xp_needed_to_objective / xp_magic
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
						
						elif tree_type == "inflamadeira":
							if ability_level >= 76:
								print("Você receberá pelo menos 200xp por lenha.\n")
								xp_blisterwood = 200
								price_for_sell = "Você não pode vender lenhas de inflamadeira."
								qtd_logs_needed = xp_needed_to_objective / xp_blisterwood
								total_profit = price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %s"%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
						
						elif tree_type == "mágica amaldiçoada":
							if ability_level >= 82:
								print("Você receberá pelo menos 275xp por lenha.\n")
								xp_cursed_magic = 275
								price_for_sell = "É um tipo especial de árvore mágica, encontrada na Terra Selvagem depois de terminar a quest.Não se pode vender lenhas amaldiçoadas, pois elas se transformam em normais."
								qtd_logs_needed = xp_needed_to_objective / xp_cursed_magic
								total_profit = price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %s"%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
							
						elif tree_type == "vinha mutante":
							if ability_level >= 83:
								print("Você receberá pelo menos 140xp por lenha.\n")
								xp_mutated_vine = 140
								price_for_sell = "Não é possível vender."
								qtd_logs_needed = xp_needed_to_objective / xp_mutated_vine
								total_profit = price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %s"%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
							
						elif tree_type == "raiz curva" or tree_type == "raiz reta":
							if ability_level >= 83:
								print("Você receberá pelo menos 161.6xp por lenha.\n")
								xp_roots = 161.6
								price_for_sell = "Não é possível vender."
								qtd_logs_needed = xp_needed_to_objective / xp_roots
								total_profit = price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %s"%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
					
						elif tree_type == "anciã":
							if ability_level >= 90:
								print("Você receberá pelo menos 325xp por lenha.\n")
								xp_elder = 325
								price_for_sell = 4896
								qtd_logs_needed = xp_needed_to_objective / xp_elder
								total_profit = qtd_logs_needed * price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %i moedas."%(total_profit))	
							
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
							
						
						elif tree_type == "cristal":
							if ability_level >= 94:
								print("Você receberá ao menos 434.5xp por lenha.\n")
								xp_crystal = 434.5
								price_for_sell = "Árvores de Cristal não fornecem lenha."
								qtd_logs_needed = xp_needed_to_objective / xp_crystal
								total_profit = price_for_sell
								print("Então, %s, você deverá cortar %i árvores de %s."%(player_name, qtd_logs_needed, tree_type))
								print("Lucro total: %s."%(total_profit))	
						
							else: 
								print("\n")
								print(red+"Você não possui o nível necessário para utilizar esse tipo de lenha.\033[0;0m")
								print("\n")
								print("A aplicação irá fechar em 2 minutos, mas se quiser, apenas reinicie.")
						
						
						print("Você gostaria de recomeçar? Digite 'sim' ou 'não'. \n")
						return_to_start = input("-> ")
						if return_to_start == "sim":
							os.system("cls") #Limpa o prompt de comando e, nesse caso, funciona apenas em sistemas operacionais Windows
							continue #Vai informar que o While pode ser carregado, recarregando assim TODO o código dentro do mesmo
						elif return_to_start == "não":
							print("A aplicação irá fechar em 2 minutos. Se desejar, feche manualmente.")
							print("Digite 'fechar' para finalizar a aplicação.\n")
							close_App = input("-> ")
							if close_App == "fechar":
								sys.exit()
							break #Vai informar que o While NÃO deve ser carregado, logo, a aplicação apenas prossegue para seus 2 minutos de vida pós-processamento
							
		except ValueError: #Nesse caso, quando o erro ValueError for disparado, ele fará isso:
			print(red+"Valor inválido.\033[0;0m")
			print("Digite 'recomeçar' para recarregar o código ou qualquer tecla para finalizar. \n")
			return_to_start = input("->  ")
			if return_to_start == "recomeçar":
				os.system("cls")
				continue
			else:
				print(blue+"\n Até mais, %s!\033[0;0m"%(player_name))
				sys.exit()
				break



time.sleep(120)		#Tempo em segundos para a aplicação fechar automaticamente
