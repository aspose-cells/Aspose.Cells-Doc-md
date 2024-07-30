---
title: Charger le classeur avec la taille de papier de l imprimante spécifiée
type: docs
weight: 430
url: /fr/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Vous pouvez spécifier la taille de papier de l'imprimante de votre choix lors du chargement de votre classeur en utilisant la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Veuillez noter que si vous créez un nouveau fichier dans MS Excel, vous verrez que la taille de papier est la même que le réglage de l'imprimante par défaut sur votre machine.

{{% /alert %}}

Le code d'exemple suivant illustre l'utilisation de la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Il crée d'abord un classeur, le sauvegarde ensuite dans un flux de mémoire au format XLSX. Ensuite, il le charge avec un format de papier A5 et le sauvegarde au format PDF. Ensuite, il le charge à nouveau avec un format de papier A3 et le sauvegarde à nouveau au format PDF. Si vous ouvrez les PDFs de sortie et vérifiez leur format de papier, vous verrez qu'ils sont différents. L'un est A5 et l'autre est A3. Veuillez télécharger le [PDF de sortie A5](PrinterSize-a5_out.pdf) et le [PDF de sortie A3](PrinterSize-a3_out.pdf) générés par le code pour votre référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
