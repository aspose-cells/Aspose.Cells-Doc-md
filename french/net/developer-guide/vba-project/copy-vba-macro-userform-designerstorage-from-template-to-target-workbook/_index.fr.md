---
title: Copier le UserForm DesignerStorage du macro VBA du modèle vers le classeur cible
type: docs
weight: 130
url: /fr/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de copier un projet VBA d'un fichier Excel dans un autre fichier Excel. Le projet VBA se compose de différents types de modules, tels que Document, Procédural, Concepteur, etc. Tous ces modules peuvent être copiés avec un code simple, mais pour le module Concepteur, il y a des données supplémentaires appelées Stockage du concepteur qui doivent être accédées ou copiées. Les deux méthodes suivantes traitent du Stockage du concepteur.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible**

Veuillez consulter le code d'exemple suivant. Il copie le projet VBA du [fichier Excel modèle](50528345.xlsm) dans un classeur vide et le sauvegarde en tant que [fichier Excel de sortie](50528346.xlsm). Si vous ouvrez le projet VBA à l'intérieur du fichier Excel modèle, vous verrez un formulaire utilisateur comme indiqué ci-dessous. Le formulaire utilisateur se compose de Stockage du concepteur, il sera donc copié en utilisant les méthodes [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) et [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La capture d'écran suivante montre le fichier Excel de sortie et ses contenus qui ont été copiés du fichier Excel modèle. Lorsque vous cliquez sur le Bouton 1, cela ouvre le formulaire utilisateur VBA qui a lui-même un bouton de commande qui affiche une boîte de dialogue lorsqu'il est cliqué.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
