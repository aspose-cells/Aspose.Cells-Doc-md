---
title: Définition du type de chiffrement fort
type: docs
weight: 60
url: /fr/net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) vous permet de chiffrer et protéger par mot de passe des feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques. Un fournisseur de services cryptographiques (ou CSP) est un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est "Office 97/2000 Compatible". Il s'agit d'un CSP avec plusieurs problèmes de sécurité connus. Les feuilles de calcul sécurisées avec le type de chiffrement "chiffrement faible (XOR)" ou avec le type de chiffrement "Office 97/2000 Compatible" peuvent être facilement crackées.

Pour résoudre ce problème, utilisez l'un des types de chiffrement forts fournis par Microsoft Excel. Vous pouvez modifier le type de chiffrement pour utiliser le CSP le plus fort disponible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise, par exemple, 'Fournisseur cryptographique Microsoft fort'.

Vous pouvez également chiffrer et protéger par mot de passe des fichiers Excel avec un type de chiffrement fort en utilisant l'API Aspose.Cells.

{{% /alert %}} 
## **Application du chiffrement avec Microsoft Excel**
Pour implémenter le chiffrement de fichier dans Microsoft Excel (par exemple 2007) :

1. Dans le menu **Outils**, sélectionnez **Options**.
1. Sélectionnez l'onglet **Sécurité**.
1. Entrez une valeur pour le champ **Mot de passe pour ouvrir**.
1. Cliquez sur **Avancé**.
1. Choisissez le type de chiffrement et confirmez le mot de passe.
## **Application du chiffrement avec Aspose.Cells**
Les exemples de code ci-dessous appliquent un chiffrement fort sur un fichier et définissent un mot de passe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
