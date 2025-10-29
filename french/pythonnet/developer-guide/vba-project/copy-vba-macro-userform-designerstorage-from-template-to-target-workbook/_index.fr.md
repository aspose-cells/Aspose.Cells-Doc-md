---
title: Copier le UserForm DesignerStorage du macro VBA du modèle vers le classeur cible
type: docs
weight: 130
url: /fr/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells pour Python via .NET vous permet de copier un projet VBA d'un fichier Excel à un autre. Le projet VBA se compose de divers types de modules, tels que Document, Procédural, Designer, etc. Tous les modules peuvent être copiés avec un code simple, mais pour le module Designer, il existe des données supplémentaires appelées Designer Storage qui doivent être accessibles ou copiées. Les deux méthodes suivantes traitent du Designer Storage.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible**

Veuillez consulter le code d'exemple suivant. Il copie le projet VBA du [fichier Excel modèle](50528345.xlsm) dans un classeur vide et le sauvegarde en tant que [fichier Excel de sortie](50528346.xlsm). Si vous ouvrez le projet VBA à l'intérieur du fichier Excel modèle, vous verrez un formulaire utilisateur comme indiqué ci-dessous. Le formulaire utilisateur se compose de Stockage du concepteur, il sera donc copié en utilisant les méthodes [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) et [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La capture d'écran suivante montre le fichier Excel de sortie et ses contenus qui ont été copiés du fichier Excel modèle. Lorsque vous cliquez sur le Bouton 1, cela ouvre le formulaire utilisateur VBA qui a lui-même un bouton de commande qui affiche une boîte de dialogue lorsqu'il est cliqué.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
