---
title: Détecter le type de lien hypertexte
type: docs
weight: 160
url: /fr/net/detect-hyperlink-type/
---
## **Détecter le type de lien hypertexte**

 Un fichier Excel peut avoir différents types d'hyperliens tels qu'externe, référence de cellule, chemin de fichier, etc. Aspose.Cells prend en charge la fonction de détection du type d'hyperlien. Les types d'hyperliens sont représentés par le[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Énumération. Le[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)L'énumération a les membres suivants.

- Externe : lien externe
- FilePath : chemin d'accès local et complet aux fichiers\dossiers.
- E-mail : E-mail
- CellReference : lien vers une cellule ou une plage nommée.

Pour vérifier le type de lien hypertexte, le[**Lien hypertexte**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) la classe offre une[**Type de lien**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) propriété avec un type de retour de[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). L'extrait de code suivant illustre l'utilisation de[**Type de lien**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)propriété en utilisant ceci[fichier excel source](94896195.xlsx).

### Code source

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Voici la sortie générée par l'extrait de code donné ci-dessus.

### Sortie console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
