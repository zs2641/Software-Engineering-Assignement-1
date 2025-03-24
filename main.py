from my_functions import build_person, build_experiment

if __name__ == "__main__":
    # Versuchsperson erstellen
    subject = build_person("Max", "Mustermann", "male", 30)

    # Versuchsleitung erstellen
    supervisor = build_person("Sophie", "Zembacher", "female", 18)

    # Experiment erstellen
    experiment = build_experiment("Herzfrequenztest", "2025-03-24", supervisor, subject)


    print(experiment)
