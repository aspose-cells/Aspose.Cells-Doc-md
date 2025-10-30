---
title: hur man anpassar UI utseende för meddelandekort i GridJs  
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-customize-toast/
description: Denna artikel beskriver hur man anpassar UI utseende för meddelandekort i GridJs.
keywords: GridJs,anpassa,kort,UI,utseende,visuellt,meddelande,varning
aliases:
aliases:
  - /java/aspose-cells-gridjs/customize-toast/
  - /java/aspose-cells-gridjs/customize-ui-alert/
  - /java/aspose-cells-gridjs/customize-message-tips/
  - /java/aspose-cells-gridjs/customize-notification/
  - /java/aspose-cells-gridjs/customize-popup-message/
  - /java/aspose-cells-gridjs/customize-ui-message/
  - /java/aspose-cells-gridjs/customize-toast-styling/
  - /java/aspose-cells-gridjs/customize-toast-theme/
  - /java/aspose-cells-gridjs/customize-message/




---

# Guide för anpassade toast-meddelanden i GridJs

## Översikt

GridJs erbjuder ett flexibelt system för anpassade toast-notifikationer som låter dig ersätta de standardmeddelanden med din egen notifieringsimplementering. Denna guide visar olika metoder för att anpassa toast-notifikationer efter ditt programs behov.

## Innehållsförteckning

- [Grundläggande användning](#basic-usage)
- [Integrations exempel](#integration-examples)
  - [Vackra anpassade toast](#1-beautiful-custom-toast)
  - [Toastr-bibliotek](#2-toastr-library-integration)
  - [SweetAlert2](#3-sweetalert2-integration)
  - [Vue + Element UI](#4-vue--element-ui)
  - [React + Ant Design](#5-react--ant-design)
- [Avancerade användningsfall](#advanced-use-cases)
  - [Loggning och analys](#6-logging-and-analytics)
  - [Mobilvänlig toast](#7-mobile-friendly-toast)
- [API-referens](#api-reference)
- [Bästa praxis](#best-practices)

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

**Parametrar:**
- `title` (sträng): Toast-notifikationens titel
- `content` (sträng): Toast-meddelandets innehåll
- `callback` (funktion, valfri): Callback-funktion att köra efter att toasten har avvisats

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

**Funktioner:**
- Gradientbakgrund
- Modalöverlagring
- Klicka för att avvisa
- Autoavslutning efter 3 sekunder
- Stängningsknapp

---

### 2. Toastr Library Integration

Integrate the popular [Toastr](https://github.com/CodeSeven/toastr) library for toast notifications.

**Prerequisites:**
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
```

**Implementering:**
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

**Anpassningsalternativ:**
- `closeButton`: Visar en stängningsknapp
- `progressBar`: Visar en nedräkningsindikator
- `positionClass`: Kontrollerar toastens position (övre höger, neder vänster, etc.)
- `timeOut`: Auto-dismiss varaktighet i millisekunder

---

### 3. SweetAlert2 Integration

Use [SweetAlert2](https://sweetalert2.github.io/) for beautiful, customizable alert dialogs.

**Prerequisites:**
```html
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
```

**Implementering:**
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

**Tillgängliga Ikoner:**
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

**Notifierings Typer:**
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

**Alternativa Ant Design-Komponenter:**
- `message.success()`
- `message.error()`
- `message.warning()`
- `notification.open()` (för mer komplexa notifieringar)

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

**Användningsområden:**
- Debug-loggning
- Användarbeteende spårning
- Felövervakning
- Prestandamått

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

**Mobiloptimeringsfunktioner:**
- Bottenplacering (tummvänlig)
- Procentbaserad bredd (max 80%)
- Kortare varaktighet (2 sekunder)
- Större tangentmål
- Ingen överlagring (icke-blockerande)

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

### 2. Icke-blockerande aviseringar

För bättre användarupplevelse, använd icke-blockerande toast-aviseringar istället för modala varningar:

```javascript
// ❌ Blocks user interaction
alert(`${title}: ${content}`);

// ✅ Non-blocking
showToastNotification(title, content);
```

### 3. Passande varaktighet

Välj lämpliga autoudlösningstider baserat på innehållets längd:

```javascript
const duration = content.length > 50 ? 5000 : 3000;
setTimeout(remove, duration);
```

### 4. Tillgänglighet

Se till att din anpassade toast är tillgänglig:

```javascript
toast.setAttribute('role', 'alert');
toast.setAttribute('aria-live', 'polite');
toast.setAttribute('aria-atomic', 'true');
```

### 5. Felhantering

Wrap din toastfunktion i try-catch för att förhindra att kalkylbladet bryts:

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

### 6. Rensa resurser

Rensa alltid DOM-element och händelselyssnare:

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

### 7. Återställ till standard vid behov

Ge en metod för att återställa standardbeteendet för toast:

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

### Minnesläckor

**Problem:** Sidan blir långsam efter många toast-aviseringar.

**Lösning:** Rensa DOM-element och eventlyssnare:
```javascript
const remove = () => {
  document.body.removeChild(toast);
  toast.onclick = null;  // Remove event listeners
  if (callback) callback();
};
```

### Mobilskärmproblem

**Problem:** Toast ser illa ut på mobila enheter.

**Lösningar:**
1. Använd procentbaserade bredder: `maxWidth: '80%'`
2. Add viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
3. Använd relativa fontstorlekar: `fontSize: '14px'` istället för fasta pixlar

---



