---
title: Enregistrement de fichiers
type: docs
weight: 20
url: /fr/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells permet de créer et de sauvegarder des fichiers, et de manipuler des fichiers existants. Cet article explique les différentes façons dont les fichiers peuvent être enregistrés.

{{% /alert %}} 
## **Différentes façons d'enregistrer des fichiers**
 Aspose.Cells fournit le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft et fournit les méthodes nécessaires pour travailler avec des fichiers Excel. La[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe fournit la[sauvegarder](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) méthode utilisée pour enregistrer les fichiers Excel. La[sauvegarder](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) La méthode a de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers de différentes manières. Le format de fichier dans lequel le fichier est enregistré est déterminé par le[Enregistrer le format](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)énumération.
## **Enregistrement du fichier à un emplacement**
 Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (complet avec le chemin de stockage) et le format de fichier souhaité (à partir du[Enregistrer le format](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)énumération) lors de l'appel du[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) objets[sauvegarder](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Enregistrement du fichier dans le flux**
 Pour enregistrer des fichiers dans un flux, créez un objet MemoryStream ou FileStream et enregistrez le fichier dans cet objet de flux en appelant le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) objets[sauvegarder](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) méthode. Spécifiez le format de fichier souhaité à l'aide de la[Enregistrer le format](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) énumération lors de l'appel du[sauvegarder](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
