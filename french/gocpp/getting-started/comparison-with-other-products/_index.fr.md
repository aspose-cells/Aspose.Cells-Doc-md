---
title: Comparaison des fonctionnalités et des performances d’Aspose.Cells pour Go via C avec Excelize, Tealeg/xlsx et Go OLE.
linktitle: Comparaison des fonctionnalités et des performances
type: docs
weight: 40
url: /fr/go-cpp/comparison-of-functionality-and-performance/
description: Comparaison des fonctionnalités et des performances d’Aspose.Cells pour Go via C avec Excelize, Tealeg/xlsx, et Go OLE.
keywords: Aspose.Cells, Excel, Fenêtre de surveillance des formules, Cellules, Ajout, C++
---

 Voici une comparaison complète d’Aspose.Cells pour Go (via C) avec d’autres bibliothèques populaires de traitement Excel en Go (Excelize, tealeg/xlsx, go-ole) en termes de fonctionnalités, performances et cas d’utilisation.

## Différences dans le positionnement et la structure de base

| Nom de la bibliothèque | Type | Implémentation sous-jacente | Dépendance CGO | Déploiement multiplateforme |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells pour Go | Bibliothèque commerciale (MIT/Payant) | Moteur natif, wrapper Go CGO | ✅ Oui | Support pour Windows, Linux |
| Excelize | Bibliothèque open source (MIT) | Implémentation pure Go | ❌ Non | Support pour Windows, Linux, MacOS |
| tealeg/xlsx | Bibliothèque open source (BSD) | Implémentation pure Go | ❌ Non | Support pour Windows, Linux, MacOS |
| go-ole | Bibliothèque open source (BSD) | Interface OLE/COM Windows en Go | ✅ Oui (seulement Windows) | Windows uniquement |

### Principuelles différences

- Aspose.Cells for Go via C++ est une bibliothèque commerciale de niveau industriel avec les fonctions les plus complètes, mais un produit payant est requis.
- Excelize est actuellement la bibliothèque Go la plus active et open source, entièrement en Go.
- Tealeg/xlsx est une bibliothèque open source ancienne avec des fonctions plus basiques et une maintenance lente.
- Go-ole est un schéma d’automatisation COM réservé à Windows qui dépend de l’installation de Excel et n’est pas recommandé pour les environnements serveurs.

## Comparaison des fonctionnalités

### Comparaison des formats de fichiers pris en charge

| Format de feuille de calcul |   Aspose.Cells for Go via C++ | Excelize    | Tealeg/xlsx | Go-OLE (Excel App)    |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx                         | ✅ Oui                        | ✅ Oui    | ✅ Oui     | ✅ Fiable sur Excel |
| Xlsb                         | ✅ Oui                        | ❌ Non    | ❌ Non     | ✅ Fiable sur Excel |
| Xls                          | ✅ Oui                        | ❌ Non    | ❌ Non     | ✅ Fiable sur Excel |
| Xlsm                         | ✅ Oui                        | ✅ Oui    | ✅ Oui     | ✅ Fiable sur Excel |
| Xltm                         | ✅ Oui                        | ✅ Oui    | ✅ Oui     | ✅ Fiable sur Excel |
| Xltx                         | ✅ Oui                        | ✅ Oui    | ✅ Oui     | ✅ Fiable sur Excel |
| Csv                          | ✅ Oui                        | ❌ Non    | ❌ Non     | ✅ Fiable sur Excel |
| Ods                          | ✅ Oui                        | ❌ Non    | ❌ Non     | ✅ Fiable sur Excel |
| Html                         | ✅ Oui                        | ❌ Non    | ❌ Non     | ❌ Non              |
| Numbers                      | ✅ Oui                        | ❌ Non    | ❌ Non     | ❌ Non              |
| Json                         | ✅ Oui                        | ❌ Non    | ❌ Non     | ❌ Non              |
| Xml                          | ✅ Oui                        | ❌ Non    | ❌ Non     | ❌ Non              |
| SpreadsheetML                | ✅ Oui                        | ❌ Non    | ❌ Non     | ❌ Non              |

### Fonctionnalités des feuilles de calcul prises en charge

| Fonctionnalités de la bibliothèque |   Aspose.Cells for Go via C++ | Excelize         | Tealeg/xlsx | Go-OLE (Excel App) |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| Lecture/écriture (supporte le format de fichier) | ✅ Oui                        | ✅ Oui          | ✅ Oui     | ✅ Oui   |
| Cellule/Ligne/Colonne/Feuille         | ✅ Oui                        | ✅ Oui          | ✅ Oui     | ✅ Oui   |
| Style                            | ✅ Oui                         | ✅ Oui          | ✅ Oui     | ✅ Oui   |
| Calcul de formule                | ✅ Oui                         | ✅ Oui (Partie)  | ❌ Non      | ✅ Oui (calculé par Excel)  |
| Graphique/Image                  | ✅ Oui                         | ✅ Oui (Partie)  | ❌ Non      | ✅ Oui   |
| TableauCroiséDynamiques          | ✅ Oui                         | ✅ Oui          | ❌ Non      | ✅ Oui   |
| Mise en forme conditionnelle     | ✅ Oui                         | ✅ Oui          | ❌ Non      | ✅ Oui   |
| Validation des données           | ✅ Oui                         | ✅ Oui          | ❌ Non      | ✅ Oui   |
| Chiffrement/protection par mot de passe | ✅ Oui                  | ✅ Oui          | ❌ Non      | ✅ Oui   |
| Validation des données           | ✅ Oui                         | ✅ Oui          | ❌ Non      | ✅ Oui   |
| Macro VBA                        | ✅ Oui Lecture                 | ❌ Non          | ❌ Non      | ✅ Oui   |
| Validation des données           | ✅ Oui                         | ✅ Oui          | ❌ Non      | ✅ Oui   |

## Comparaison de performance

- **Environnement de test** :
Processeur : Intel(R) Core(TM) i7-12700 12e génération (2,10 GHz)
RAM installée : 64,0 GB (63,7 GB utilisables)
Nom de l’OS : Microsoft Windows 11 Pro
Version de l’OS : 10.0.26100
Architecture de l’OS : 64 bits
Version de Go : go version go1.24.5 windows/amd64
Aspose.Cells for Go via C++ : 25.9.0
Excelize : 1.4.1

- **Scénario de test** : Supposons un fichier volumineux, 10 feuilles de calcul, 100 000 lignes x 250 colonnes, y compris la mise en forme

- **Résultats d'exécution** :
  - Excelize s'exécute pendant 35 minutes (Heure de début : 2025-10-09T10:04:16+08:00, Heure de fin : 2025-10-09T10:39:53+08:00), taille du fichier généré : 1,11 Go.
  - Aspose.Cells for Go via C++(modèle 1) s'exécute pendant 27 minutes (Heure de début : 2025-10-09T10:57:55+08:00, Heure de fin : 2025-10-09T11:16:24+08:00), taille du fichier généré : 936 Mo.
  - Aspose.Cells for Go via C++(modèle 2) s'exécute pendant 16 minutes (Heure de début : 2025-10-09T12:01:26+08:00, Heure de fin : 2025-10-09T12:17:17+08:00), taille du fichier généré : 1,16 Go.
