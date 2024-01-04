# Guide d'Utilisation de la Suite de Tests IDS CAN Bootloader

Ce document sert de guide pour l'utilisation de la suite de tests pour le projet IDS CAN Bootloader.

## Pré-requis

Avant de commencer, assurez-vous d'avoir installé les dépendances nécessaires listées dans le fichier `requirements.txt`. Pour installer ces dépendances, utilisez la commande suivante dans votre terminal :

```shell
$ pip install -r requirements.txt
```

## Structure de l'Arborescence des Tests

Le répertoire `tests/` contient tous les tests relatifs au projet. Voici un aperçu des composants clés :

- `test_basic_functionality/`: Tests pour les fonctionnalités de base du bootloader.
- `test_system_topology/`: Tests pour le comportement du bootloader en topologie système.
- `conftest.py`: Configuration globale des tests. **Ne pas modifier**.
- `setup.py`: Script pour la configuration des tests.

## Exécution des Tests

Pour lancer la suite de tests, utilisez la commande suivante :

```shell
$ python -m pytest
```

### Options de Test

- Pour exécuter tous les tests dans un sous-dossier spécifique, par exemple `test_basic_functionality`, utilisez :

  ```shell
  $ python -m pytest tests/test_basic_functionality
  ```

- Pour exécuter un test spécifique, indiquez le chemin du fichier de test :

  ```shell
  $ python -m pytest tests/test_basic_functionality/test_protocol.py
  ```

### Tests en Développement

- Les tests en cours de développement sont situés dans le dossier `ongoing/`. Pour les exécuter :

  ```shell
  $ python -m pytest tests/ongoing
  ```

## Ajout de Tests Personnalisés

Pour ajouter vos propres tests :

1. Créez un fichier Python dans `tests/`, commençant par `test_`.
2. À l'intérieur, définissez une ou plusieurs fonctions de test, également préfixées par `test_`.

Exemple :

```python
# contenu du fichier tests/test_my_custom_tests.py
import pytest

def test_custom_functionality():
    assert my_custom_function() == expected_result
```

## Pour les Développeurs Pressés

Pour lancer rapidement des tests :

```shell
$ pip install -r requirements.txt
$ python -m pytest tests/test_basic_functionality
```

N'oubliez pas de spécifier le sous-dossier de tests approprié.

## Documentation Supplémentaire

Pour plus d'informations sur l'utilisation de `pytest`, consultez la [documentation officielle](https://docs.pytest.org/).
