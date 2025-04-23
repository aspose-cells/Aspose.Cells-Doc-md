---
title: Détecter le type d hyperlien
type: docs
weight: 160
url: /fr/net/detect-hyperlink-type/
description: Apprenez comment détecter le type d hyperlien à travers l API Aspose.Cells for .NET.
keywords: Détecter le type d hyperlien, Détecter le type d hyperlien, Obtenir le type d hyperlien
---

## **Détecter le type d'hyperlien**

Un fichier Excel peut comporter différents types d'hyperliens tels que des liens externes, des références de cellules, des chemins de fichiers, etc. Aspose.Cells prend en charge la fonctionnalité de détection du type d'hyperlien. Les types d'hyperliens sont représentés par l'énumération [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). L'énumération [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) comporte les membres suivants.

- Externe : Lien externe
- Chemin de fichier : Chemin local et complet vers les fichiers/dossiers.
- E-mail : E-mail
- Référence de cellule : Lien vers une cellule ou une plage nommée.

Pour vérifier le type d'hyperlien, la classe [**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) fournit une propriété [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) avec un type de retour de [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). L'extrait de code suivant montre l'utilisation de la propriété [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) en utilisant ce [fichier Excel source](94896195.xlsx).

### Code source

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
