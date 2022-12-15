---
title: Installer Aspose.Cells sur Windows
type: docs
weight: 20
url: /fr/net/installing-aspose-cells-on-windows/
---
{{% alert color="primary" %}} 

 Parfois, vous pouvez rencontrer des problèmes lors de l'installation**Aspose.Cells** en utilisant son package d'installation (Aspose.Cells.msi...Windows Installer Package) sur**Windows vue** . Ce document explique comment nous pouvons y faire face et mettre en œuvre l'installation réussie du composant. Réellement**Aspose.Cells**Le programme d'installation doit créer un dossier virtuel sur IIS pour le déploiement de ses démos Web (Asp.NET Demos) sur votre machine, vous devez donc disposer de privilèges d'administration avant l'installation**Aspose.Cells** à l'aide de son installateur. Le programme d'installation demande un accès de niveau administrateur au système doit être explicitement autorisé à le faire.

{{% /alert %}} 
## **Facteurs possibles**
 Normalement, dans**Windows vue** , les produits/composants que vous installez/utilisez sont toujours implémentés sous les autorisations "utilisateur normal", même si vous êtes un**Administrateur** . Les programmes n'ont qu'un accès limité au système de fichiers, même si vous êtes connecté en tant que**Administrateur** . Cela a des effets secondaires malheureux que vous ne rencontreriez normalement pas dans Windows XP lorsque vous êtes connecté en tant que**Administrateur**.
## **UAC (contrôle de compte d'utilisateur)**
**UAC** est la partie de**Windows vue** qui vous demande la permission. La**UAC** mode (également appelé**Mode d'approbation administrateur** ) est un mode de fonctionnement qui affecte (principalement) le fonctionnement des comptes administrateur. Lorsque**UAC**est activé (ce qui est le cas par défaut), vous devez explicitement donner l'autorisation à tout programme qui souhaite utiliser les pouvoirs "administrateur". Tout programme qui essaie d'utiliser les pouvoirs d'administrateur sans votre permission se verra refuser l'accès.**UAC** est également requis pour d'autres fonctions de sécurité de**Windows vue** , y compris**Mode protégé** dans Internet Explorer. Le mode protégé d'Internet Explorer protège votre ordinateur des pages Web malveillantes et d'autres vulnérabilités liées au Web, y compris celles qui sont inconnues.

 Lorsque**UAC** est activé, chaque programme que vous exécutez ne recevra qu'un accès "utilisateur standard" au système, même lorsque vous êtes connecté en tant qu'administrateur.**Windows vue** a la capacité intégrée de réduire automatiquement le potentiel de failles de sécurité dans le système. Il le fait en activant automatiquement cette fonctionnalité appelée**Contrôle de compte d'utilisateur** (ou**UAC** pour faire court). La**UAC**force les utilisateurs qui font partie du groupe d'administrateurs locaux à s'exécuter comme s'ils étaient des utilisateurs réguliers sans privilèges administratifs. Bien que**UAC** améliore nettement la sécurité sur**Windows vue** , dans certains scénarios, vous souhaiterez peut-être le désactiver, par exemple lorsque vous donnez des démos devant un public (des démos qui ne sont pas liées à la sécurité, par exemple). Certains utilisateurs à domicile pourraient être tentés de désactiver**UAC** en raison de l'utilisation de ressources supplémentaires de leur système.
## **Étapes impliquées pour une installation réussie du composant**
-  Veuillez vous assurer que IIS est installé sur votre Vista avant d'installer**Aspose.Cells** . Il est obligatoire car**Aspose.Cells** Le programme d'installation doit créer un dossier virtuel sur IIS pour le déploiement des démos Web (Asp.NET Demos).
-  Vous devez désactiver**UAC** (Contrôle de compte d'utilisateur). Vous devez vous assurer que vous disposez d'un**Les privilèges d'administrateur** avec un contrôle total du système avant l'installation**Aspose.Cells** . Sinon, vous pourriez obtenir une erreur # 2869 lors de l'installation**Aspose.Cells**à l'aide de son installateur.

Voici quelques façons d'y parvenir.
### **Utilisation de la ligne de commande**
1.  Recherchez cmd.exe dans votre répertoire Windows, puis cliquez dessus avec le bouton droit de la souris et sélectionnez Exécuter en tant que...**Administrateur**
 2. Maintenant, exécutez la commande suivante à l'invite de commande : msiexec /i<your path>/Aspose.Cells.msi et Entrée.
### **Utilisation du panneau de configuration**
- Cliquez sur Démarrer
- Cliquez sur Panneau de configuration
- Cliquez sur Comptes d'utilisateurs et sécurité familiale
- Cliquez sur Comptes d'utilisateurs
- Cliquez sur Activer ou désactiver le contrôle de compte d'utilisateur
- Décochez la case
- Cliquez sur OK

{{% alert color="primary" %}} 

Vous devrez redémarrer votre ordinateur pour que la modification prenne effet. Ce changement affecte tous les comptes sur l'ordinateur, pas seulement le vôtre.

{{% /alert %}}
