# Question 8: Pesticide Database Query
pesticides = {'Roundup': {'active_ingredient': 'Glyphosate', 'application_rate': 1.5},'Paraquat': {'active_ingredient': 'Paraquat', 'application_rate': 0.5},'Glyphosate 480SL': {'active_ingredient': 'Glyphosate', 'application_rate': 1.8}}
glyphosate_pesticides = [trade_name for trade_name, details in pesticides.items() if details['active_ingredient'] == 'Glyphosate']
print(f"Pesticides with Glyphosate as active ingredient: {', '.join(glyphosate_pesticides)}")
