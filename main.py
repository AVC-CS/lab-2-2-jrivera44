def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
    regular_rate = 18.25
    overtime_rate = 27.78
    regular_hours = 40
    overtime_hours = hours - regular_hours
    
    regular_wage = overtime_rate * overtime_hours
    total_wage = regular_wage + overtime_wage
    overtimewage = 50
   ##################################################
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {reg_hours} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
