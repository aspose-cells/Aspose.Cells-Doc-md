---
title: Le fichier de licence ne fonctionne plus
type: docs
weight: 60
url: /fr/net/license-file-not-working-anymore/
---
## **Symptôme**

 Parfois, les utilisateurs sont frustrés car leurs fichiers de licence ne fonctionnent plus lorsqu'ils déplacent/publient leur(s) projet(s) Web vers un nouveau serveur. Ils se sentent contrariés car leurs fichiers de licence fonctionnaient correctement sur leur ancien (ancien) serveur, mais maintenant ils obtiennent un supplément**Avertissement relatif aux droits d'auteur** feuille de calcul de filigrane (chaque fois qu'ils génèrent des rapports à l'aide du composant) sur le nouvel environnement de serveur.

### **Un scénario**

"Nous avons utilisé Aspose.Cells sur notre projet Web ASP.NET pour générer/manipuler des rapports Excel, nous avons obtenu une licence valide que nous utilisons. Il y a quelques jours, nous avons déplacé le site Web vers un nouveau serveur ; il n'y a eu aucune mise à niveau ou modification, nous nous nous sommes assurés et avons simplement déplacé chaque fichier vers le nouveau serveur, y compris le fichier Aspose.Cells.dll et le ou les fichiers .lic associés. Maintenant, lorsque nous essayons de générer des rapports Excel dans le nouvel environnement de serveur, nous obtenons un**Avertissement relatif aux droits d'auteur** feuille de filigrane sur nos rapports. Nous avons essayé de télécharger et d'installer un nouveau fichier de licence à partir de la section Mes commandes du site, mais cela n'a pas du tout résolu le problème. Pour votre information, nous implémentons la licence en plaçant le fichier Aspose.Cells.lic dans le dossier bin du site avec le fichier composant Aspose.Cells.dll, qui, comme je l'ai mentionné, fonctionnait sans problème sur l'ancien serveur."

### **La solution**

Aspose dispose d'un mécanisme de licence propre et fiable. Généralement, le problème doit être lié à un problème de déploiement. Si un fichier de licence fonctionne correctement (sur un serveur), il devrait également fonctionner correctement sur d'autres serveurs/environnements. Normalement, les utilisateurs utilisent l'application_Démarrer ou session_Démarrez les événements, etc. dans le fichier global.asax pour y placer le code de licence. Il est donc tout à fait possible que l'Application_Début / Séance_Les événements de démarrage ne sont pas déclenchés pour traiter le code de licence sur leurs nouveaux emplacements. Il est à noter ici que Aspose.Cells lèvera toujours une exception si le composant ne trouve pas le fichier de licence dans un chemin. Les utilisateurs doivent s'assurer que le code de licence (où qu'ils se trouvent) soit traité et que des événements soient déclenchés dans lesquels ils insèrent le code de licence. L'utilisateur peut redémarrer le service associé, c'est-à-dire "Publication sur le Web" et essayer de savoir si Application_Début / Séance_Les événements de démarrage sont déclenchés lorsqu'ils visitent leurs projets sur le nouvel environnement de serveur.

### **Confirmation**

Veuillez également vous assurer que…

- Vous utilisez un fichier de licence valide dans votre projet.
- Vous ou quelqu'un d'autre ne devez pas éditer / modifier le fichier de licence, sinon le fichier de licence ne fonctionnera pas.
- Vous devez être conscient de l'expiration de votre abonnement de licence (vous pouvez simplement ouvrir le fichier lic dans le bloc-notes et vérifier la date d'expiration).
-  Vous n'utilisez pas une version (Aspose.Cells.dll) publiée après l'expiration de votre abonnement de licence. Il convient de noter ici qu'un fichier de licence n'expire jamais, mais si vous utilisez la version du composant publiée après l'expiration de votre abonnement, vous obtiendrez un supplément**Avertissement relatif aux droits d'auteur** feuille de filigrane chaque fois que vous créez un fichier Excel.

### **Les références**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
