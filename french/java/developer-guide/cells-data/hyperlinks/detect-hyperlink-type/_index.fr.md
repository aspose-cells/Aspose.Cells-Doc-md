---
title: Détecter le type de lien hypertexte
type: docs
weight: 180
url: /fr/java/detect-hyperlink-type/
---
## **Détecter le type de lien hypertexte**

Un fichier Excel peut avoir différents types d'hyperliens tels qu'externe, référence de cellule, chemin de fichier, etc. Aspose.Cells prend en charge la fonction de détection du type d'hyperlien. Les types d'hyperliens sont représentés par le[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Énumération. Le[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)L'énumération a les membres suivants.

- [**EXTERNE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Lien externe
- [**CHEMIN DU FICHIER**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): chemin local et complet vers les fichiers\dossiers.
- [**E-MAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): E-mail
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): lien vers une cellule ou une plage nommée.

Pour vérifier le type de lien hypertexte, le[**Lien hypertexte**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) la classe offre une[**Type de lien**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) propriété avec un type de retour de[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). L'extrait de code suivant illustre l'utilisation de[**Type de lien**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)propriété en utilisant ceci[fichier excel source](LinkTypes.xlsx).

## Code source

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Voici la sortie générée par l'extrait de code donné ci-dessus.

## Sortie console
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
