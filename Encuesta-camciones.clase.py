class MusicQuiz:
    def __init__(self):
        self.questions = [
            ("1: Cual es el nombre del vocalista de Queen?", ["Freddie Mercury", "David Bowie", "Michael Jackson"], 1),
            
            ("2: Qué banda compuso la cancion 'Thunder'?", ["Imagine Dragons", "Linkin Park", "Skillet"], 1),
            
            ("3: Que cancion de Linkin Park se escucha en Transformers 2?", ["Lost", "Don´t Stay", "New Divide"], 3),
            
            ("4: Que banda es conocida por la cancion 'Bohemian Rhapsody'?", ["Queen", "Led Zeppelin", "Pink Floyd"], 1),
            
            ("5: Cancion más escuchada de divididos?", ["Cancion animal", "El 38", "Fuel"], 2),
            
            ("6: Qué banda presentó la cancion 'Enter Sadman'?", ["AC/DC", "Fall Out Boy", "Metallica"], 3),
            
            ("7: De qué banda es la cancion 'Chop Suey!?", ["System Of A Down", "Catupecu Machu", "Three Days Grace"], 1),
            
            ("8: Cancion famosa de pelicula 8 Mile, de Eminem?", ["The Real Slim Shady", "Lose Yourself", "Rap God"], 2),
            
            ("9: Que cancion de Katy Perry se escucha en Madagascar 3?", ["Firework", "Last Friday Night", "California Girls"], 1),
            
            ("10: Que cancion de AC/DC se escuha en la película de Iron Man?", ["T.N.T", "Shoot to thrill", "Thunderstruck"], 2)
        ]
        self.current_question = 0
        self.score = 0

    def ask_question(self):
        question, options, correct_answer = self.questions[self.current_question]
        print(f"\n{question}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        while True:
            try:
                user_answer = int(input("Your answer (1, 2, or 3): "))
                if 1 <= user_answer <= 3:
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")

        self.current_question += 1

    def play(self):
        while self.current_question < len(self.questions):
            self.ask_question()

        print(f"Excelente. Respondiste correctamente {self.score} de {len(self.questions)} preguntas.")

quiz = MusicQuiz()
quiz.play()