tasks= input("Enter your tasks for today separated by a comma: ").split(", ")
done_tasks= []
ongoing_tasks=[]
for D in tasks:
    print(f"\n {D} \n")
    achivement= input(f"Did you finish {D} already? (Yes/No): ").lower()
    if achivement == "yes":
        print("Nice job!")
        done_tasks.append(D)
    else:
        print("Try not to put it off!")
        ongoing_tasks.append(D)
    print("-----------")
progress= input("Do you want to see your today's progress? (Yes/No): ").lower()

if progress == "yes":
    print("           ⁎⁎⁎⁎⁎⁎⁎⁎ Done Tasks ⁎⁎⁎⁎⁎⁎⁎⁎ ")
    print(done_tasks)
    print("\n         ⁎⁎⁎⁎⁎⁎⁎⁎ ongoing tasks ⁎⁎⁎⁎⁎⁎⁎⁎")
    print(ongoing_tasks)
else:
    input("Please hit Enter to exit....")