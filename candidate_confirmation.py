
class candidate:
    def verify_candidate(self):
        selected_candidates = ["Vikesh Shrivastav", "Rajdeep Shah", "Tushar Patil", "Nilesh Panchal"]
        self.name1 = input("Enter your name here !! ")
        # self.email = input("Enter your email address !!")
        for i in selected_candidates:
            if self.name1 == i or i.lower() or i.capitalize():
                print(f"Congratulations !! {self.name1} , you are selected a Candidate,\n")
                break
            else:
                print(f"Who the F*** are you, get away of this session {self.name1}")
                quit()

class verified(candidate):
    def job_details(self):
        candidate.verify_candidate(self)
        self.work = "Capgeminin technologies pvt ltd"
        self.location = "Mumbai"
        self.jobTime = "10AM to 7PM"
        print(f"""Hey as you are selected,
         you have to join office from 1st of next month.
         Mr {self.name1} your job location will be {self.location} at 
        {self.work} and the job timing is {self.jobTime}, Thanks""")




if __name__ == "__main__":
    x = verified()
    x.job_details()