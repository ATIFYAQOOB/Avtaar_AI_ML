header = ['Movie_name','Director_name','Release_date','Overall_gross_earning','The_cast']
with open('assignmwnt_2.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(main_list)