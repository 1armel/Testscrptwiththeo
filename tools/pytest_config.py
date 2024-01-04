#!/usr/bin/env python
# pytest_config.py
# Configuration globale pour les tests du projet IDS CAN Bootloader
"""
Ce fichier configure pytest pour ajouter une option de ligne de commande personnalisée --scope, qui peut être utilisée pour limiter les tests à un certain ensemble, comme les tests de base (basic), les tests de topologie système (system), ou tous les tests (all). La fonction pytest_addoption est utilisée pour ajouter cette option, et le fixture test_scope fournit un moyen d'accéder à la valeur de cette option dans vos tests.
"""

import pytest

# Configuration de pytest pour utiliser des options et des paramètres spécifiques au projet

def pytest_addoption(parser):
    """
    Ajoute des options de ligne de commande spécifiques au projet.
    """
    # Exemple : Ajout d'une option pour spécifier un sous-ensemble de tests
    parser.addoption("--scope", action="store", default="all",
                     help="Spécifie le scope de test à exécuter (par exemple, 'basic', 'system', ou 'all')")

@pytest.fixture
def test_scope(request):
    """
    Un fixture pour accéder à la valeur de l'option de scope de test.
    """
    return request.config.getoption("--scope")

# Vous pouvez ajouter d'autres configurations ou fixtures globales si nécessaire
