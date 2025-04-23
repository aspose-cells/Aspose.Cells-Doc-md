---
title: Détecter le type d hyperlien
type: docs
weight: 180
url: /fr/java/detect-hyperlink-type/
---

## **Détecter le type d'hyperlien**

Un fichier Excel peut avoir différents types d'hyperliens comme externe, référence de cellule, chemin de fichier, etc. Aspose.Cells prend en charge la fonctionnalité pour détecter le type d'hyperlien. Les types d'hyperliens sont représentés par l'Enumération [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). L'Enumération [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType) a les membres suivants.

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL) : Lien externe
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE-PATH) : Chemin local et chemin complet vers les fichiers/dossiers.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL) : E-mail
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL-REFERENCE) : Lien vers une cellule ou une plage nommée.

Pour vérifier le type d'hyperlien, la classe [**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) fournit une [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) propriété avec un type de retour de [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Le code suivant illustre l'utilisation de la propriété [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) en utilisant ce [fichier Excel source](LinkTypes.xlsx).

## Code source

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Ce qui suit est le résultat généré par le code donné ci-dessus.

## Sortie de la console
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
{{< app/cells/assistant language="java" >}}
