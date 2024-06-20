---
title: Obtenir des avertissements pour la substitution de police lors du rendu de fichiers Excel en PDF
type: docs
weight: 120
url: /fr/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

Parfois, lors du rendu de fichiers Microsoft Excel au format PDF, Aspose.Cells remplace les polices. Aspose.Cells fournit une fonctionnalité qui permet aux développeurs de savoir qu'une police particulière a été remplacée en déclenchant une alerte. Il s'agit d'une fonctionnalité utile qui peut vous aider à identifier pourquoi le PDF rendu par Aspose.Cells est différent du fichier Excel réel et vous pouvez ensuite prendre les mesures nécessaires. Par exemple, vous pouvez installer les polices manquantes pour que les résultats de rendu soient identiques.

Si vous souhaitez obtenir les avertissements de remplacement de police lors du rendu d'un fichier Excel au format PDF, implémentez l'interface IWarningCallback et définissez la méthode PdfSaveOptions.setWarningCallback() avec votre interface implémentée.

{{% /alert %}}

La capture d'écran ci-dessous montre le fichier Excel source utilisé dans le code suivant. Il contient du texte dans les cellules A6 et A7 dans des polices qui ne sont pas bien rendues par Microsoft Excel.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells va substituer les polices dans les cellules A6 et A7 par des polices appropriées comme indiqué ci-dessous.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Télécharger le fichier source et le PDF de sortie**

Vous pouvez télécharger le fichier Excel source et le PDF de sortie à partir des liens suivants

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

Le code suivant implémente la méthode [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) et définit la méthode [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) avec l'interface implémentée. Désormais, chaque fois qu'une police sera remplacée dans une cellule, Aspose.Cells déclenchera une alerte à l'intérieur de la méthode WarningCallback.warning().

{{< highlight java >}}

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

## **Sortie des Avertissements**

Après la conversion du fichier source, les avertissements suivants sont affichés dans la console de débogage :

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode Workbook.calculateFormula juste avant de rendre la feuille de calcul au format PDF. Cela permettra de recalculer les valeurs dépendantes des formules et de rendre les bonnes valeurs dans le PDF. 

{{% /alert %}}
