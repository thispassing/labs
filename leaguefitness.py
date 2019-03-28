death_exercises_dict = {"Push-ups":1, "Plank":4, "Side Plank":2}
loss_exercise_dict = {"Wall Squat":15, "Lunges":2, "Standing Squats":10}
win_exercise_dict = {"Sun Salutation":1, "Wrist Streching":1, "Hip Stretching":1}
game_number = 3


while True:
    print(f"\nThat is game number {game_number}")
    win_loss = str(input("Win? (y/n): "))
    deaths = int(input("Number of deaths: "))
    if game_number % 3 == 1:
        pushup_number = deaths*death_exercises_dict["Push-ups"]
        print(f"\nDeaths penalty.  Do {pushup_number} push-ups.")
        if win_loss == "n":
            wallsquat_number = loss_exercise_dict["Wall Squat"]
            print(f"Wall squat for {wallsquat_number} seconds.")
        else:
            sun_number = win_exercise_dict["Sun Salutation"]
            print(f"{sun_number} Sun Salutation(s).")
    elif game_number % 3 == 2:
        plank_number = deaths*death_exercises_dict["Plank"]
        print(f"\nDeaths penalty. Plank for {plank_number} seconds")
        if win_loss == "n":
            lunges_number = loss_exercise_dict["Lunges"]
            print(f"Do {lunges_number} lunges.")
        else:
            wrist_number = win_exercise_dict["Wrist Streching"]
            print(f"Wrist stretching for {wrist_number} minute(s).")
    elif game_number % 3 == 0:
        sideplank_number = deaths*death_exercises_dict["Side Plank"]
        print(f"\nDeaths penalty. Side plank for {sideplank_number} seconds, then do the other side.")
        if win_loss == "n":
            standingsquats_number = loss_exercise_dict["Standing Squats"]
            print(f"Do {standingsquats_number} standing squats.")
        else:
            hip_number = win_exercise_dict["Hip Stretching"]
            print(f"Hip streching for {hip_number} minute(s).")
    else:
        print("error")
    
    # so that i don't miss 
    if deaths !=0:
        game_number+=1



