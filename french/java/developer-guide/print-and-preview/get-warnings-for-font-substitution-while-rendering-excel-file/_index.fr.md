---
title: Obtenir des avertissements pour la substitution de polices lors du rendu du fichier Excel
type: docs
weight: 120
url: /fr/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

Parfois, lors du rendu de fichiers Excel Microsoft au format PDF, Aspose.Cells remplace les polices. Aspose.Cells fournit une fonctionnalité qui permet aux développeurs de savoir qu'une police particulière a été remplacée en déclenchant un avertissement. Il s'agit d'une fonctionnalité utile qui peut vous aider à identifier pourquoi le PDF rendu Aspose.Cells est différent du fichier Excel réel et vous pouvez ensuite prendre les mesures appropriées. Par exemple, vous pouvez installer les polices manquantes afin que les résultats du rendu soient identiques.

Si vous souhaitez obtenir les avertissements de substitution de police lors du rendu d'un fichier Excel au format PDF, implémentez l'interface IWarningCallback et définissez la méthode PdfSaveOptions.setWarningCallback() avec votre interface implémentée.

{{% /alert %}}

La capture d'écran ci-dessous montre le fichier Excel source utilisé dans le code suivant. Il contient du texte dans les cellules A6 et A7 dans des polices qui ne sont pas bien rendues par Microsoft Excel.

![tâche : image_autre_texte](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells remplacera les polices dans les cellules A6 et A7 par des polices appropriées, comme indiqué ci-dessous.

![tâche : image_autre_texte](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Télécharger le fichier source et le PDF de sortie**

Vous pouvez télécharger le fichier Excel source et le PDF de sortie à partir des liens suivants

- [source.xlsx](5472700.xlsx)
- [sortie.pdf](5472699.pdf)

 Le code suivant implémente le[**IAvertissementCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) et réglez le[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) méthode avec l'interface implémentée. Désormais, chaque fois qu'une police sera remplacée dans une cellule, Aspose.Cells déclenchera un avertissement dans la méthode WarningCallback.warning().

{{< highlight "java" >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **Sortie d'avertissements**

Après la conversion du fichier source, les avertissements suivants s'affichent sur la console de débogage :

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode Workbook.calculateFormula juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
