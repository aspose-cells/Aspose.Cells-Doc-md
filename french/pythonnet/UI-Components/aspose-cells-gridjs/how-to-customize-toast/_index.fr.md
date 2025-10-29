---
title: comment personnaliser l apparence UI pour l info bulle de message dans GridJs  
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/how-to-customize-toast/
description: Cet article explique comment personnaliser l apparence UI pour la notification toast dans GridJs.
keywords: GridJs, personnaliser, toast, UI, apparence, visuel, message, alerte
aliases:
aliases:
  - /python-net/aspose-cells-gridjs/customize-toast/
  - /python-net/aspose-cells-gridjs/customize-ui-alert/
  - /python-net/aspose-cells-gridjs/customize-message-tips/
  - /python-net/aspose-cells-gridjs/customize-notification/
  - /python-net/aspose-cells-gridjs/customize-popup-message/
  - /python-net/aspose-cells-gridjs/customize-ui-message/
  - /python-net/aspose-cells-gridjs/customize-toast-styling/
  - /python-net/aspose-cells-gridjs/customize-toast-theme/
  - /python-net/aspose-cells-gridjs/customize-message/




---

# Guide de toaster personnalisé pour GridJs

## Aperçu

GridJs offre un système de notifications toast personnalisé flexible qui vous permet de remplacer les messages toast par défaut par votre propre implémentation de notification. Ce guide présente diverses approches pour personnaliser les notifications toast selon les besoins de votre application.

## Table des matières

- [Utilisation de base](#basic-usage)
- [Exemples d'intégration](#integration-examples)
  - [Superbes toasts personnalisés](#1-beautiful-custom-toast)
  - [Bibliothèque Toastr](#2-toastr-library-integration)
  - [SweetAlert2](#3-sweetalert2-integration)
  - [Vue + Element UI](#4-vue--element-ui)
  - [React + Ant Design](#5-react--ant-design)
- [Cas d'utilisation avancés](#advanced-use-cases)
  - [Journalisation et analytique](#6-logging-and-analytics)
  - [Toast adapté aux mobiles](#7-mobile-friendly-toast)
- [Référence API](#api-reference)
- [Meilleures Pratiques](#best-practices)

---

## Basic Usage

### Simple Alert Example

The most basic custom toast can be implemented using the native `alert()` function:

```javascript
const xs = x_spreadsheet('#spreadsheet');

// Define custom toast function
function myToast(title, content, callback) {
  alert(`${title}: ${content}`);
  if (callback) callback();
}

// Set custom toast
xs.customToast(myToast);
```

**Paramètres :**
- `title` (chaîne) : Titre de la notification toast
- `content` (chaîne) : Contenu du message toast
- `callback` (fonction, optionnel) : Fonction de rappel à exécuter après la fermeture du toast

---

## Integration Examples

### 1. Beautiful Custom Toast

Create a visually appealing toast notification without external dependencies:

```javascript
function beautifulToast(title, content, callback) {
  // Create dimmer overlay
  const dimmer = document.createElement('div');
  Object.assign(dimmer.style, {
    position: 'fixed',
    top: 0, left: 0, right: 0, bottom: 0,
    background: 'rgba(0,0,0,0.5)',
    zIndex: 9999
  });

  // Create toast element
  const toast = document.createElement('div');
  Object.assign(toast.style, {
    position: 'fixed',
    top: '50%', left: '50%',
    transform: 'translate(-50%, -50%)',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
    padding: '20px 30px',
    borderRadius: '10px',
    boxShadow: '0 10px 40px rgba(0,0,0,0.3)',
    zIndex: 10000,
    minWidth: '300px'
  });

  toast.innerHTML = `
    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-weight: bold;">
      <span>${title}</span>
      <span class="close" style="cursor: pointer;">×</span>
    </div>
    <div>${content}</div>
  `;

  const remove = () => {
    document.body.removeChild(toast);
    document.body.removeChild(dimmer);
    if (callback) callback();
  };

  toast.querySelector('.close').onclick = remove;
  dimmer.onclick = remove;

  document.body.appendChild(dimmer);
  document.body.appendChild(toast);

  // Auto-dismiss after 3 seconds
  setTimeout(remove, 3000);
}

xs.customToast(beautifulToast);
```

**Fonctionnalités :**
- Fond en dégradé
- Superposition modale
- Cliquer pour fermer
- Fermeture automatique après 3 secondes
- Bouton de fermeture

---

### 2. Toastr Library Integration

Integrate the popular [Toastr](https://github.com/CodeSeven/toastr) library for toast notifications.

**Prerequisites:**
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
```

**Mise en œuvre :**
```javascript
xs.customToast((title, content, callback) => {
  toastr.options = {
    closeButton: true,
    progressBar: true,
    positionClass: 'toast-top-right',
    timeOut: 3000
  };
  toastr.info(content, title);
  if (callback) callback();
});
```

**Options de personnalisation :**
- `closeButton` : Affiche un bouton de fermeture
- `progressBar` : Affiche une barre de progression countdown
- `positionClass` : Contrôle la position de l'alerte (haut-droite, bas-gauche, etc.)
- `timeOut` : Durée de fermeture automatique en millisecondes

---

### 3. SweetAlert2 Integration

Use [SweetAlert2](https://sweetalert2.github.io/) for beautiful, customizable alert dialogs.

**Prerequisites:**
```html
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
```

**Mise en œuvre :**
```javascript
xs.customToast((title, content, callback) => {
  Swal.fire({
    title: title,
    html: content,
    icon: 'info',
    confirmButtonText: 'OK'
  }).then(() => {
    if (callback) callback();
  });
});
```

**Icones disponibles :**
- `success`
- `error`
- `warning`
- `info`
- `question`

---

### 4. Vue + Element UI

Integration with Vue.js and Element UI's notification component.

```javascript
new Vue({
  el: '#app',
  mounted() {
    const xs = x_spreadsheet('#spreadsheet');

    xs.customToast((title, content, callback) => {
      this.$notify({
        title: title,
        message: content,
        type: 'info',
        duration: 3000,
        onClose: callback
      });
    });
  }
});
```

**Types de notifications :**
- `success`
- `warning`
- `info`
- `error`

---

### 5. React + Ant Design

Integration with React and Ant Design's message component.

```javascript
import { message } from 'antd';

const App = () => {
  useEffect(() => {
    const xs = x_spreadsheet('#spreadsheet');

    xs.customToast((title, content, callback) => {
      message.info({
        content: `${title}: ${content}`,
        duration: 3,
        onClose: callback
      });
    });
  }, []);

  return <div id="spreadsheet"></div>;
};
```

**Composants Ant Design alternatifs :**
- `message.success()`
- `message.error()`
- `message.warning()`
- `notification.open()` (pour des notifications plus complexes)

---

## Advanced Use Cases

### 6. Logging and Analytics

Combine custom toast with logging and analytics tracking:

```javascript
xs.customToast((title, content, callback) => {
  // Log to console
  console.log(`[Toast] ${title}:`, content);

  // Track in analytics system
  if (window.analytics) {
    analytics.track('toast_shown', {
      title: title,
      content: content,
      timestamp: new Date().toISOString()
    });
  }

  // Display custom notification
  showMyCustomToast(title, content, callback);
});
```

**Cas d'utilisation :**
- Journalisation de débogage
- Suivi du comportement de l'utilisateur
- Surveillance des erreurs
- Mesures de performance

---

### 7. Mobile-Friendly Toast

Create a mobile-optimized toast notification:

```javascript
function mobileToast(title, content, callback) {
  const toast = document.createElement('div');
  Object.assign(toast.style, {
    position: 'fixed',
    bottom: '20px',
    left: '50%',
    transform: 'translateX(-50%)',
    background: '#323232',
    color: 'white',
    padding: '12px 24px',
    borderRadius: '24px',
    fontSize: '14px',
    zIndex: 10000,
    maxWidth: '80%',
    textAlign: 'center',
    boxShadow: '0 4px 12px rgba(0,0,0,0.3)'
  });

  toast.textContent = `${title}: ${content}`;
  document.body.appendChild(toast);

  setTimeout(() => {
    document.body.removeChild(toast);
    if (callback) callback();
  }, 2000);
}

xs.customToast(mobileToast);
```

**Fonctionnalités d'optimisation mobile :**
- Positionnement en bas (adapté au pouce)
- Largeur en pourcentage (max 80%)
- Durée plus courte (2 secondes)
- Cibles de tap plus grandes
- Pas de superposition (non bloquant)

---

## API Reference

### `customToast(toastFunction)`

Sets a custom toast notification function for the spreadsheet instance.

**Parameters:**
- `toastFunction` (Function | null): Custom toast function with signature `(title, content, callback) => void`
  - Pass `null` to restore default toast behavior

**Returns:**
- The spreadsheet instance (for method chaining)

**Example:**
```javascript
// Set custom toast
xs.customToast(myToastFunction);

// Restore default
xs.customToast(null);

// Method chaining
xs.customToast(myToast)
  .loadData(data)
  .setActiveSheet(0);
```

---

## Best Practices

### 1. Always Handle the Callback

Ensure you call the callback function if provided, as it may contain important cleanup or continuation logic:

```javascript
function myToast(title, content, callback) {
  // ... show toast ...
  if (callback) callback();  // ✅ Always call
}
```

### 2. Notifications non bloquantes

Pour une meilleure expérience utilisateur, utilisez des notifications toast non bloquantes au lieu d'alertes modales :

```javascript
// ❌ Blocks user interaction
alert(`${title}: ${content}`);

// ✅ Non-blocking
showToastNotification(title, content);
```

### 3. Durée appropriée

Choisissez des durées de fermeture automatique appropriées en fonction de la longueur du contenu :

```javascript
const duration = content.length > 50 ? 5000 : 3000;
setTimeout(remove, duration);
```

### 4. Accessibilité

Assurez-vous que votre toast personnalisé soit accessible :

```javascript
toast.setAttribute('role', 'alert');
toast.setAttribute('aria-live', 'polite');
toast.setAttribute('aria-atomic', 'true');
```

### 5. Gestion des erreurs

Encapsulez votre fonction toast dans un try-catch pour éviter de casser la feuille de calcul :

```javascript
xs.customToast((title, content, callback) => {
  try {
    // Your toast implementation
    myCustomToast(title, content);
  } catch (error) {
    console.error('Toast error:', error);
  } finally {
    if (callback) callback();
  }
});
```

### 6. Nettoyage des ressources

Nettoyez toujours les éléments DOM et les écouteurs d'événements :

```javascript
function myToast(title, content, callback) {
  const toast = document.createElement('div');
  // ... setup toast ...

  const remove = () => {
    document.body.removeChild(toast);
    // Clean up any event listeners
    toast.onclick = null;
    if (callback) callback();
  };

  document.body.appendChild(toast);
  setTimeout(remove, 3000);
}
```

### 7. Restaurer par défaut en cas de besoin

Fournir un moyen de restaurer le comportement par défaut des notifications toast :

```javascript
// Set custom toast
xs.customToast(myToast);

// Later, restore default
xs.customToast(null);
```

---

## Troubleshooting

### Toast Not Showing

**Problem:** Custom toast function is called but nothing appears.

**Solutions:**
1. Check z-index values (ensure they're higher than spreadsheet elements)
2. Verify the toast element is appended to `document.body`
3. Check browser console for JavaScript errors

### Callback Not Working

**Problem:** Operations after toast don't execute.

**Solution:** Ensure you're calling the callback function:
```javascript
if (callback) callback();  // Don't forget this!
```

### Fuites de mémoire

**Problème :** La page devient lente après de nombreuses notifications toast.

**Solution :** Nettoyez les éléments DOM et les écouteurs d'événements :
```javascript
const remove = () => {
  document.body.removeChild(toast);
  toast.onclick = null;  // Remove event listeners
  if (callback) callback();
};
```

### Problèmes d'affichage mobile

**Problème :** Les toasts ont un mauvais rendu sur les appareils mobiles.

**Solutions :**
1. Utilisez des largeurs en pourcentage : `maxWidth: '80%'`
2. Add viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
3. Utilisez des tailles de police relatives : `fontSize: '14px'` au lieu de pixels fixes

---



