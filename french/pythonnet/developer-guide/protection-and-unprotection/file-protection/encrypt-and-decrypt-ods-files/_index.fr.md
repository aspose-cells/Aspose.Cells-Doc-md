---
title: Crypter et décrypter les fichiers ODS
type: docs
weight: 10
url: /fr/python-net/encrypt-and-decrypt-ods-files/
description: protéger par mot de passe et chiffrer des fichiers ODS en utilisant Aspose.Cells pour Python via .NET, une bibliothèque purement .NET.
---

{{% alert color="primary" %}}
OpenOffice.org est une suite bureautique complète qui prend en charge la protection par mot de passe et le chiffrement des fichiers. Cependant, un fichier ODS chiffré ne peut être ouvert que par OpenOffice après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS chiffré et peut afficher un message d'avertissement. Les options de chiffrement ne s'appliquent pas aux fichiers ODS contrairement aux autres types de fichiers. 
Aspose.Cells pour Python via .NET permet de chiffrer et déchiffrer des fichiers ODS. Les fichiers ODS déchiffrés peuvent être ouverts dans Excel et OpenOffice. 
{{% /alert %}}

## **Chiffrer avec OpenOffice Calc**
1. Sélectionnez **Enregistrer sous** et cochez la case **Enregistrer avec mot de passe**.
1. Cliquez sur le bouton **Enregistrer**.
1. Saisissez votre mot de passe souhaité dans les champs **Entrer le mot de passe pour ouvrir** et **Confirmer le mot de passe** dans la fenêtre Définir le mot de passe qui s'ouvre. 
1. Cliquez sur le bouton **OK** pour enregistrer le fichier.

## **Chiffrer un fichier ODS avec Aspose.Cells pour Python via .NET**
Pour chiffrer un fichier ODS, chargez le fichier et définissez la valeur [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) comme mot de passe réel avant de l'enregistrer. Le fichier ODS chiffré en sortie ne pourra être ouvert que dans OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Déchiffrer un fichier ODS avec Aspose.Cells pour Python via .NET**

Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Une fois le fichier chargé, définissez la chaîne [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) comme nulle.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
