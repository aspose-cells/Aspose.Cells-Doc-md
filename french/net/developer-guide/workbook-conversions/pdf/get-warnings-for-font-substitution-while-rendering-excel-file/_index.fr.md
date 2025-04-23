---
title: Obtenir des avertissements pour la substitution de police lors du rendu de fichiers Excel en PDF
type: docs
weight: 230
url: /fr/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

Parfois, lors du rendu d'un fichier Microsoft Excel en PDF, Aspose.Cells substitue des polices. Aspose.Cells propose une fonctionnalité qui permet aux développeurs de savoir quelle police particulière a été substituée en déclenchant un avertissement. Il s'agit d'une fonctionnalité utile qui peut vous aider à identifier pourquoi un PDF créé par Aspose.Cells semble différent du fichier Excel d'origine afin que vous puissiez prendre des mesures appropriées. Par exemple, installer les polices manquantes pour que les résultats du rendu soient identiques.

{{% /alert %}} 

Pour obtenir des avertissements pour la substitution de police lors du rendu de fichiers Excel en PDF, implémentez l'interface IWarningCallback et définissez la propriété PdfSaveOptions.WarningCallback avec votre interface implémentée.

La capture d'écran ci-dessous montre un fichier Excel source que nous utiliserons dans le code suivant. Il contient du texte dans les cellules A6 et A7 dans des polices qui ne sont pas rendues correctement par Microsoft Excel.

|**Toutes les polices ne sont pas rendues correctement**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells va substituer les polices dans les cellules A6 et A7 par des polices appropriées comme indiqué ci-dessous.

|**Polices substituées**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Télécharger le fichier source et le PDF de sortie**
Vous pouvez télécharger le fichier Excel source et le PDF de sortie à partir des liens suivants

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **Code**
Le code suivant met en œuvre l'IWarningCallback et définit la propriété PdfSaveOptions.WarningCallback avec l'interface implémentée. Maintenant, chaque fois qu'une police sera substituée dans une cellule, Aspose.Cells déclenchera un avertissement à l'intérieur de la méthode WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Sortie**
Après avoir converti le fichier Excel source en PDF, les avertissements sont affichés dans la console de débogage comme ceci :

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode Workbook.CalculateFormula juste avant de générer la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes des formules seront recalculées et les valeurs correctes seront générées dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
