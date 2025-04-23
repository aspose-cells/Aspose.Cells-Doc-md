---
title: Charger le classeur avec la taille de papier de l imprimante spécifiée
type: docs
weight: 430
url: /fr/net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Vous pouvez spécifier la taille de papier de l'imprimante de votre choix lors du chargement de votre classeur en utilisant la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize). Veuillez noter que si vous créez un nouveau fichier dans MS Excel, vous verrez que la taille de papier est la même que le réglage de l'imprimante par défaut sur votre machine.

{{% /alert %}}

Le code d'exemple suivant illustre l'utilisation de la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize). Il crée d'abord un classeur, puis le sauvegarde dans un flux de mémoire au format XLSX. Ensuite, il le charge avec une taille de papier A5 et le sauvegarde au format PDF. Ensuite, il le charge à nouveau avec une taille de papier A3 et le sauvegarde à nouveau au format PDF. Si vous ouvrez les PDF de sortie et vérifiez leur taille de papier, vous verrez qu'ils sont différents. L'un est en A5 et l'autre en A3. Veuillez télécharger le [PDF de sortie en A5](5115234.pdf) et le [PDF de sortie en A3](5115233.pdf) générés par le code pour votre référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
