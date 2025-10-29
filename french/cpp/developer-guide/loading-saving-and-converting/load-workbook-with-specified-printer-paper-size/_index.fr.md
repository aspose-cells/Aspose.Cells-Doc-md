---
title: Charger le classeur avec la taille de papier de l imprimante spécifiée
type: docs
weight: 430
url: /fr/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Vous pouvez spécifier la taille de papier de l'imprimante de votre choix lors du chargement de votre classeur en utilisant la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Veuillez noter que si vous créez un nouveau fichier dans MS Excel, vous verrez que la taille de papier est la même que le réglage de l'imprimante par défaut sur votre machine.

{{% /alert %}}

Le code d'exemple suivant illustre l'utilisation de la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Il crée d'abord un classeur, puis le sauvegarde en mémoire dans un format XLSX. Ensuite, il le charge avec une taille de papier A5 et le sauvegarde en PDF. Ensuite, il le recharge avec une taille de papier A3 et le sauvegarde à nouveau en PDF. Si vous ouvrez les PDF de sortie et vérifiez leur taille de papier, vous verrez qu'elles diffèrent. L'un est A5 et l'autre A3. Téléchargez les [PDF de sortie A5](PrinterSize-a5_out.pdf) et [PDF de sortie A3](PrinterSize-a3_out.pdf) générés par le code pour référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
