---
title: Crypter et décrypter les fichiers ODS
type: docs
weight: 10
url: /fr/java/encrypt-and-decrypt-ods-files/
description: protégez par mot de passe et cryptez les fichiers ODS à l'aide de Aspose.Cells for Java qui est une pure bibliothèque Java.
---
{{% alert color="primary" %}}
OpenOffice.org est une suite bureautique complète qui prend en charge la protection par mot de passe et le cryptage des fichiers. Cependant, le fichier ODS crypté ne peut être ouvert par OpenOffice qu'après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS crypté et peut générer un message d'avertissement. Les options de cryptage ne s'appliquent pas au fichier ODS contrairement aux autres types de fichiers.
 Aspose.Cells permet de chiffrer et de déchiffrer le fichier ODS. Le fichier ODS décrypté peut être ouvert à la fois dans Excel et OpenOffice,
{{% /alert %}}

## **Crypter avec OpenOffice Calc**
1.  Sélectionner**Enregistrer sous** et cliquez sur le**Enregistrer avec mot de passe** boîte.
1.  Clique le**sauvegarder** bouton.
1.  Tapez votre mot de passe souhaité dans les deux**Entrez le mot de passe pour ouvrir** et**Confirmez le mot de passe** champs dans la fenêtre Définir le mot de passe qui s'ouvre.
1.  Clique le**D'ACCORD** bouton pour enregistrer le fichier.

## **Chiffrement/déchiffrement du fichier ODS :**

 Pour chiffrer un fichier ODS, chargez le fichier et transmettez le mot de passe réel à[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)avant de le sauvegarder. Le fichier ODS crypté de sortie ne peut être ouvert que dans OpenOffice. Pour déchiffrer un fichier ODS, chargez le fichier en fournissant le mot de passe dans le[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . Une fois le fichier chargé, appelez la fonction[**Classeur.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) avec le mot de passe réel comme argument et enfin passer null à[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Exemple de code :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
