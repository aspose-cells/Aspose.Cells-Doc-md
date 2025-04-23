---
title: Crypter et décrypter les fichiers ODS
type: docs
weight: 10
url: /fr/net/encrypt-and-decrypt-ods-files/
description: Protégez par mot de passe et chiffrez les fichiers ODS à l aide d Aspose.Cells pour .Net, qui est une bibliothèque .Net pure.
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

## **Chiffrer un fichier ODS avec Aspose.Cells pour .Net**
Pour chiffrer un fichier ODS, chargez le fichier et définissez la valeur [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) comme mot de passe réel avant de l'enregistrer. Le fichier ODS chiffré en sortie ne pourra être ouvert que dans OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Déchiffrer un fichier ODS avec Aspose.Cells pour .Net**

Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). Une fois le fichier chargé, définissez la chaîne [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) comme nulle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
