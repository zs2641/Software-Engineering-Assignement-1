from datetime import date


def erstelle_experimente(erster_experiment_id: int):
    """
    Die Funktion erstellt eine Liste von Experimenten mit IDs, die alle die gleichen
    Versuchsleiter und Erstellungsdatum haben.

    Eingabe: erster_experiment_id: Die erste ID des Experiments
    Ausgabe: Liste von Dictionaries, die jeweils ein Experiment darstelllen
    """
    experimente: List[Dict[str, str]] = []
    heute: str = date.today().isoformat()
    
    for i in range(10):
        experiment: Dict[str, str] = {
            "Id_Nummer": erster_experiment_id + i,
            "Versuchsleiter": "Sophie Zembacher",
            "Erstellungsdatum": heute
        }
        experimente.append(experiment)
    
    return experimente


def hauptprogramm():
    """
    Die Funktion fragt nach der ersten Experiment-ID, erstellt Experimente
    und zeigt die Ergebnisse an.
    """
    try:
        erster_experiment_id: int = int(input("Geben Sie die erste Experiment-ID ein: "))
    except ValueError:
        print("Fehler: Die ID muss eine ganze Zahl sein.")
        return
    
    experimente: List[Dict[str, str]] = erstelle_experimente(erster_experiment_id)
    
    print("Erste fünf Experimente:")
    for experiment in experimente[:5]:
        print(experiment)
    
    gerade_id_anzahl: int = sum(1 for exp in experimente if exp["Id_Nummer"] % 2 == 0)
    print(f"Anzahl der Experimente mit gerader ID: {gerade_id_anzahl}")

hauptprogramm()
 
