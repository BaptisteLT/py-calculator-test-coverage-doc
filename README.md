INSTALLER LE PROJET:

1) Créer une environnement virtuel:

python -m venv venv

2) Activer l'environnement virtuel:

    Windows:
        venv\Scripts\activate

    Mac/Linux:
        source venv/bin/activate

3) Installer les dépendances:

    pip install -r requirements.txt

4) Pour lancer les tests:
    pytest .\testCalculator.py

5) Pour générer le test de coverage:
    coverage run -m pytest .\testCalculator.py
 
 6) Pour générer la documentation:
    pdoc --html --output-dir docs .\calculator.py

7) Pour run les tests de coverage à envoyer à sonarqube:
    pytest testCalculator.py --cov=calculator --cov-report=xml
    puis faire la commande: sonar-scanner