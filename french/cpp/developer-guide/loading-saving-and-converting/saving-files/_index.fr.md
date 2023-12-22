---
title: Enregistrer des fichiers
type: docs
weight: 20
url: /fr/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells permet de créer et de sauvegarder des fichiers, et de manipuler des fichiers existants. Cet article explique les différentes manières dont les fichiers peuvent être enregistrés.

{{% /alert %}} 
##  **Différentes façons de sauvegarder des fichiers**
 Aspose.Cells fournit le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft et fournit les méthodes nécessaires pour travailler avec des fichiers Excel. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe fournit le[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) méthode utilisée pour enregistrer les fichiers Excel. Le[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) La méthode comporte de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers de différentes manières. Le format de fichier dans lequel le fichier est enregistré est déterminé par le[EnregistrerFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)énumération.
##  **Enregistrer le fichier à un emplacement**
Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (avec le chemin de stockage) et le format de fichier souhaité (à partir du[EnregistrerFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) énumération) lors de l'appel du[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objets[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **Enregistrer le fichier en streaming**
 Pour enregistrer des fichiers dans un flux, créez un objet MemoryStream ou FileStream et enregistrez le fichier dans cet objet de flux en appelant le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objets[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) méthode. Spécifiez le format de fichier souhaité à l'aide du[EnregistrerFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) énumération lors de l'appel du[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
