---
title: Charger le classeur avec le format de papier d'imprimante spécifié
type: docs
weight: 430
url: /fr/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 Vous pouvez spécifier le format de papier d'imprimante de votre choix lors du chargement de votre classeur à l'aide de la[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) méthode. Veuillez noter que si vous créez un nouveau fichier dans MS Excel, vous constaterez que le format de papier est le même que le paramètre de l'imprimante par défaut de votre machine.

{{% /alert %}}

 L'exemple de code suivant illustre l'utilisation de[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) méthode. Il crée d'abord un classeur, puis l'enregistre dans un flux de mémoire au format XLSX. Ensuite, il le charge avec du papier au format A5 et l'enregistre au format PDF. Ensuite, il le charge à nouveau avec du papier au format A3 et l'enregistre à nouveau au format PDF. Si vous ouvrez les fichiers PDF de sortie et vérifiez leur format de papier, vous verrez qu'ils sont différents. L'un est A5 et l'autre est A3. Veuillez télécharger le[Sortie PDF A5](5115234.pdf) et[Sortie PDF A3](5115233.pdf) généré par le code pour votre référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
