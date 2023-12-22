---
title: Détecter le type de lien hypertexte
type: docs
weight: 160
url: /fr/net/detect-hyperlink-type/
description: Apprenez à détecter le type de lien hypertexte via le Aspose.Cells for .NET API.
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **Détecter le type de lien hypertexte**

 Un fichier Excel peut avoir différents types de liens hypertexte comme externes, référence de cellule, chemin de fichier, etc. Aspose.Cells prend en charge la fonctionnalité permettant de détecter le type de lien hypertexte. Les types d'hyperliens sont représentés par le[**Type de mode cible**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Énumération. Le[**Type de mode cible**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)L'énumération comprend les membres suivants.

- Externe : Lien externe
- FilePath : chemin local et complet vers les fichiers/dossiers.
- Courriel : Courriel
- CellReference : lien vers une cellule ou une plage nommée.

 Pour vérifier le type de lien hypertexte, le[**Lien hypertexte**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) la classe fournit un[**Type de lien**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) propriété avec un type de rendement de[**Type de mode cible**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). L'extrait de code suivant illustre l'utilisation de[**Type de lien**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)propriété en utilisant ceci[fichier Excel source](94896195.xlsx).

###  Code source

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Ce qui suit est le résultat généré par l'extrait de code donné ci-dessus.

###  Sortie console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
