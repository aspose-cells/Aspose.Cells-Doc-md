---
title: come personalizzare l aspetto dell interfaccia utente per il toast message in GridJs  
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/how-to-customize-toast/
description: Questo articolo descrive come personalizzare l aspetto dell interfaccia utente per il toast messaggio in GridJs.
keywords: GridJs,personalizza,toast,UI,aspetto,visivo,messaggio,allerta
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

# Guida personalizzata al Toast per GridJs

## Panoramica

GridJs offre un sistema di notifiche toast personalizzabili e flessibili che ti permette di sostituire i messaggi toast predefiniti con le tue notifiche personalizzate. Questa guida dimostra vari approcci per personalizzare le notifiche toast in base alle esigenze della tua applicazione.

## Indice dei Contenuti

- [ Uso di base](#basic-usage)
- [ Esempi di integrazione](#integration-examples)
  - [ Toast personalizzato bellissimo](#1-beautiful-custom-toast)
  - [ Libreria Toastr](#2-toastr-library-integration)
  - [ SweetAlert2](#3-sweetalert2-integration)
  - [Vue + Element UI](#4-vue--element-ui)
  - [React + Ant Design](#5-react--ant-design)
- [Casi d'uso avanzati](#advanced-use-cases)
  - [Registrazione e analisi](#6-logging-and-analytics)
  - [ Toast compatibile con dispositivi mobili](#7-mobile-friendly-toast)
- [Riferimento API](#api-reference)
- [Migliori pratiche](#best-practices)

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

**Parametri:**
- `title` (stringa): Il titolo della notifica toast
- `content` (stringa): Il contenuto del messaggio toast
- `callback` (funzione, opzionale): Funzione di callback da eseguire dopo la chiusura del toast

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

**Caratteristiche:**
- Sfondo a gradiente
- Overlay modale
- Clicca per chiudere
- Auto-dismiss dopo 3 secondi
- Bottone di chiusura

---

### 2. Toastr Library Integration

Integrate the popular [Toastr](https://github.com/CodeSeven/toastr) library for toast notifications.

**Prerequisites:**
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
```

**Implementazione:**
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

**Opzioni di personalizzazione:**
- `closeButton`: Mostra un pulsante di chiusura
- `progressBar`: Mostra una barra di avanzamento con conto alla rovescia
- `positionClass`: Controlla la posizione del toast (top-right, bottom-left, ecc.)
- `timeOut`: Durata di auto-dismiss in millisecondi

---

### 3. SweetAlert2 Integration

Use [SweetAlert2](https://sweetalert2.github.io/) for beautiful, customizable alert dialogs.

**Prerequisites:**
```html
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
```

**Implementazione:**
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

**Icone Disponibili:**
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

**Tipi di Notifica:**
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

**Componenti Alternativi di Ant Design:**
- `message.success()`
- `message.error()`
- `message.warning()`
- `notification.open()` (per notifiche più complesse)

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

**Casi d'uso:**
- Registrazione di debug
- Monitoraggio del comportamento dell'utente
- Monitoraggio degli errori
- Metriche delle prestazioni

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

**Funzionalità di ottimizzazione mobile:**
- Posizionamento in basso (facile da usare con il pollice)
- Larghezza basata sulla percentuale (massimo 80%)
- Durata più breve (2 secondi)
- Target di tap più grandi
- Nessuna sovrapposizione (non bloccante)

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

### 2. Notifiche non bloccanti

Per una migliore esperienza utente, utilizza notifiche toast non bloccanti invece di avvisi modali:

```javascript
// ❌ Blocks user interaction
alert(`${title}: ${content}`);

// ✅ Non-blocking
showToastNotification(title, content);
```

### 3. Durata appropriata

Scegli durate di auto-dismiss appropriate in base alla lunghezza del contenuto:

```javascript
const duration = content.length > 50 ? 5000 : 3000;
setTimeout(remove, duration);
```

### 4. Accessibilità

Assicurati che il tuo toast personalizzato sia accessibile:

```javascript
toast.setAttribute('role', 'alert');
toast.setAttribute('aria-live', 'polite');
toast.setAttribute('aria-atomic', 'true');
```

### 5. Gestione degli errori

Avvolgi la funzione toast in try-catch per evitare di bloccare il foglio di calcolo:

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

### 6. Pulizia delle risorse

Pulisci sempre gli elementi DOM e gli ascoltatori di eventi:

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

### 7. Ripristina default quando necessario

Fornire un modo per ripristinare il comportamento predefinito della notifica toast:

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

### Perdita di memoria

**Problema:** La pagina diventa lenta dopo molte notifiche toast.

**Soluzione:** Pulire gli elementi DOM e gli ascoltatori di eventi:
```javascript
const remove = () => {
  document.body.removeChild(toast);
  toast.onclick = null;  // Remove event listeners
  if (callback) callback();
};
```

### Problemi di visualizzazione su dispositivi mobili

**Problema:** Toast dall'aspetto brutto sui dispositivi mobili.

**Soluzioni:**
1. Usa larghezze percentuali: `maxWidth: '80%'`
2. Add viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
3. Usa dimensioni di carattere relative: `fontSize: '14px'` invece di pixel fissi

---



