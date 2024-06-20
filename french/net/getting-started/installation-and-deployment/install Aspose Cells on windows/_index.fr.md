---
title: Installer Aspose.Cells sur Windows
type: docs
weight: 20
url: /fr/net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

Parfois, vous pourriez rencontrer des problèmes lors de l'installation d'**Aspose.Cells** à l'aide de son package d'installation (Aspose.Cells.msi... Package Windows Installer) sur **Windows Vista**. Ce document explique comment nous pouvons y faire face et mettre en œuvre l'installation réussie du composant. En fait, l'installateur **Aspose.Cells** a besoin de créer un dossier virtuel sur IIS pour le déploiement de ses démos Web (démos Asp.NET) sur votre machine, donc vous devez avoir des privilèges d'administration avant d'installer **Aspose.Cells** à l'aide de son installateur. L'installateur exige un accès de niveau administrateur au système doit être explicitement autorisé à le faire.

{{% /alert %}} 
## **Facteurs possibles**
Normalement, sous **Windows Vista**, les produits/composants que vous installez/utilisez sont toujours mis en œuvre sous des permissions de «utilisateur normal», même si vous êtes un **administrateur**. Les programmes ne sont autorisés qu'un accès limité au système de fichiers, même si vous êtes connecté en tant qu'**administrateur**. Cela a quelques effets secondaires malheureux que vous ne rencontreriez normalement pas sous Windows XP lorsque vous êtes connecté en tant qu'**administrateur**.
## **UAC (Contrôle de compte d'utilisateur)**
**UAC** fait partie de **Windows Vista** qui vous demande la permission. Le mode **UAC** (également connu sous le nom de **mode d'approbation d'administrateur**) est un mode de fonctionnement qui affecte principalement la manière dont les comptes administrateur fonctionnent. Lorsque **UAC** est activé (ce qui est le cas par défaut), vous devez donner explicitement la permission à tout programme qui veut utiliser des pouvoirs d'«administrateur». Tout programme qui tente d'utiliser des pouvoirs d'administration sans votre permission se verra refuser l'accès. **UAC** est également requis pour d'autres fonctionnalités de sécurité de **Windows Vista**, y compris le **mode protégé** dans Internet Explorer. Le mode protégé d'Internet Explorer protège votre ordinateur contre les pages web malveillantes et d'autres vulnérabilités liées au web, y compris les inconnues.

Lorsque le mode **UAC** est activé, chaque programme que vous exécutez aura seulement un accès de «utilisateur standard» au système, même lorsque vous êtes connecté en tant qu'administrateur. **Windows Vista** a la possibilité intégrée de réduire automatiquement le potentiel de violations de sécurité dans le système. Il le fait en activant automatiquement cette fonction appelée **Contrôle du compte d'utilisateur** (ou **UAC** pour faire court). **UAC** oblige les utilisateurs faisant partie du groupe d'administrateurs locaux à fonctionner comme s'ils étaient des utilisateurs réguliers sans privilèges administratifs. Bien que **UAC** améliore clairement la sécurité sur **Windows Vista**, dans certains scénarios, vous voudrez peut-être le désactiver, par exemple lorsque vous faites des démonstrations devant un public (démonstrations qui ne sont pas liées à la sécurité, par exemple). Certains utilisateurs domestiques pourraient être tentés de désactiver **UAC** en raison de l'utilisation de ressources supplémentaires de leur système.
## **Étapes nécessaires pour une installation réussie du composant**
- Assurez-vous que IIS est installé sur votre Vista avant d'installer **Aspose.Cells**. C'est obligatoire car l'installateur **Aspose.Cells** doit créer un dossier virtuel sur IIS pour le déploiement des démos Web (démos Asp.NET).
- Vous devez désactiver le **UAC** (Contrôle du compte d'utilisateur). Vous devez vous assurer que vous avez des **privilèges administratifs** avec un contrôle total du système avant d'installer **Aspose.Cells**. Sinon, vous pourriez rencontrer une erreur # 2869 lors de l'installation d'**Aspose.Cells** à l'aide de son installateur.

Voici quelques façons d'y parvenir.
### **Utilisation de la ligne de commande**
1. Recherchez cmd.exe dans votre répertoire Windows, puis faites un clic droit dessus et sélectionnez Exécuter en tant que... Administrateur
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **Utilisation du Panneau de configuration**
- Cliquez sur Démarrer
- Cliquez sur Panneau de configuration
- Cliquez sur Comptes d'utilisateur et Sécurité familiale
- Cliquez sur Comptes d'utilisateur
- Cliquez sur Activer ou désactiver le contrôle de compte d'utilisateur
- Décochez la case
- Cliquez sur OK

{{% alert color="primary" %}} 

Vous devrez redémarrer votre ordinateur pour que le changement prenne effet. Ce changement affecte tous les comptes sur l'ordinateur, pas seulement le vôtre.

{{% /alert %}}
