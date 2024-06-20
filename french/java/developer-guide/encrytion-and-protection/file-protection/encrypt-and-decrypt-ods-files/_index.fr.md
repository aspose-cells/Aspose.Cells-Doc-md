---
title: Crypter et décrypter les fichiers ODS
type: docs
weight: 10
url: /fr/java/encrypt-and-decrypt-ods-files/
description: protéger par mot de passe et crypter les fichiers ODS à l aide de Aspose.Cells for Java qui est une bibliothèque Java pure.
---

{{% alert color="primary" %}}
OpenOffice.org est une suite bureautique complète qui prend en charge la protection par mot de passe et le chiffrement des fichiers. Cependant, un fichier ODS chiffré ne peut être ouvert que par OpenOffice après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS chiffré et peut afficher un message d'avertissement. Les options de chiffrement ne s'appliquent pas aux fichiers ODS contrairement aux autres types de fichiers. 
Aspose.Cells permet de chiffrer et de décrypter les fichiers ODS. Le fichier ODS décrypté peut être ouvert à la fois dans Excel et OpenOffice. 
{{% /alert %}}

## **Chiffrer avec OpenOffice Calc**
1. Sélectionnez **Enregistrer sous** et cochez la case **Enregistrer avec mot de passe**.
1. Cliquez sur le bouton **Enregistrer**.
1. Saisissez votre mot de passe souhaité dans les champs **Entrer le mot de passe pour ouvrir** et **Confirmer le mot de passe** dans la fenêtre Définir le mot de passe qui s'ouvre. 
1. Cliquez sur le bouton **OK** pour enregistrer le fichier.

## **Chiffrage et déchiffrage de fichier ODS :**

Pour chiffrer un fichier ODS, chargez le fichier et transmettez le mot de passe réel à [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) avant de l'enregistrer. Le fichier ODS chiffré en sortie ne peut être ouvert que dans OpenOffice. Pour déchiffrer un fichier ODS, chargez le fichier en fournissant le mot de passe à [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password). Une fois le fichier chargé, appelez la fonction [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String)) avec le mot de passe réel comme argument, puis transmettez null à [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Code exemple :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
