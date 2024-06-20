---
title: Détecter le type d hyperlien
type: docs
weight: 160
url: /fr/python-net/detect-hyperlink-type/
description: Apprenez à détecter le type de lien hypertexte via l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Détecter le type de lien hypertexte Python, Détecter le type de lien hypertexte en Python, Obtenir le type de lien hypertexte Python.
---

## **Détecter le type d'hyperlien**

Un fichier Excel peut avoir différents types de liens hypertexte tels que externes, références de cellules, chemins de fichiers, etc. Aspose.Cells pour Python via .NET prend en charge la fonction pour détecter le type de lien hypertexte. Les types de liens hypertexte sont représentés par l'énumération [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). L'énumération [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) comprend les membres suivants.

- EXTERNAL: Lien externe
- FILE_PATH: Chemin d'accès local et complet vers les fichiers/dossiers.
- EMAIL: E-mail
- CELL_REFERENCE: Lien vers une cellule ou une plage nommée.

Pour vérifier le type d'hyperlien, la classe [**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) fournit une propriété [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) avec un type de retour de [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). L'extrait de code suivant montre l'utilisation de la propriété [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) en utilisant ce [fichier Excel source](94896195.xlsx).

### Code source

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

Ce qui suit est le résultat généré par le code donné ci-dessus.

### Sortie de la Console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
