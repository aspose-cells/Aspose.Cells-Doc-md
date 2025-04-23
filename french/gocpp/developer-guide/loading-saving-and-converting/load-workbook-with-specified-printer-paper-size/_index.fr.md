---
title: Charger le classeur avec la taille de papier de l imprimante spécifiée
type: docs
weight: 430
url: /fr/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Vous pouvez spécifier la taille du papier de l'imprimante de votre choix lors du chargement de votre classeur en utilisant la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Notez que si vous créez un nouveau fichier dans MS Excel, la taille du papier sera la même que celle du paramètre par défaut de votre imprimante.

{{% /alert %}}

Le code d'exemple suivant illustre l'utilisation de la méthode [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Il crée d'abord un classeur, puis le sauvegarde dans un flux mémoire au format XLSX. Ensuite, il le charge avec une taille de papier A5 et le sauvegarde en format PDF. Ensuite, il le recharge avec une taille de papier A3 et le sauvegarde à nouveau en PDF. Si vous ouvrez les PDF de sortie et vérifiez leur taille de papier, vous verrez qu'elles sont différentes. L’un est A5 et l’autre A3. Veuillez télécharger le [PDF de sortie A5](PrinterSize-a5_out.pdf) et le [PDF de sortie A3](PrinterSize-a3_out.pdf) générés par le code pour référence.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
