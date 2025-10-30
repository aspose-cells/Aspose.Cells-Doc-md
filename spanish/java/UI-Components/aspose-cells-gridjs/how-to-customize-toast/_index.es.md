---
title: cómo personalizar la apariencia de la interfaz para el mensaje de toque en GridJs  
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-customize-toast/
description: Este artículo describe cómo personalizar la apariencia de la interfaz para las notificaciones toast en GridJs.
keywords: GridJs,personalizar,toast,UI,apariencia,visual,mensaje,alerta
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

# Guía de Toast Personalizado para GridJs

## Resumen

GridJs ofrece un sistema flexible de notificaciones toast personalizables que te permite reemplazar los mensajes toast predeterminados con tu propia implementación de notificación. Esta guía muestra varios enfoques para personalizar las notificaciones toast según las necesidades de tu aplicación.

## Tabla de Contenidos

- [Uso Básico](#basic-usage)
- [Ejemplos de Integración](#integration-examples)
  - [Hermoso Toast Personalizado](#1-beautiful-custom-toast)
  - [Biblioteca Toastr](#2-toastr-library-integration)
  - [SweetAlert2](#3-sweetalert2-integration)
  - [Vue + Element UI](#4-vue--element-ui)
  - [React + Ant Design](#5-react--ant-design)
- [Casos de Uso Avanzados](#advanced-use-cases)
  - [Registro y Análisis](#6-logging-and-analytics)
  - [ Tostada compatible con dispositivos móviles](#7-mobile-friendly-toast)
- [Referencia de API](#api-reference)
- [Mejores prácticas](#best-practices)

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

**Parámetros:**
- `title` (cadena): Título de la notificación de tostada
- `content` (cadena): Contenido del mensaje de tostada
- `callback` (función, opcional): Función de devolución de llamada para ejecutar después de descartar la tostada

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

**Funciones:**
- Fondo degradado
- Superposición modal
- Clic para cerrar
- Cierre automático después de 3 segundos
- Botón de cierre

---

### 2. Toastr Library Integration

Integrate the popular [Toastr](https://github.com/CodeSeven/toastr) library for toast notifications.

**Prerequisites:**
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
```

**Implementación:**
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

**Opciones de personalización:**
- `closeButton`: Muestra un botón de cierre
- `progressBar`: Muestra una barra de progreso de cuenta regresiva
- `positionClass`: Controla la posición de la tostada (arriba-derecha, abajo-izquierda, etc.)
- `timeOut`: Duración en milisegundos para cierre automático

---

### 3. SweetAlert2 Integration

Use [SweetAlert2](https://sweetalert2.github.io/) for beautiful, customizable alert dialogs.

**Prerequisites:**
```html
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
```

**Implementación:**
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

**Íconos disponibles:**
- `éxito`
- `error`
- `advertencia`
- `info`
- `pregunta`

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

**Tipos de Notificación:**
- `éxito`
- `advertencia`
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

**Componentes Alternativos de Ant Design:**
- `message.success()`
- `message.error()`
- `message.warning()`
- `notification.open()` (para notificaciones más complejas)

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

**Casos de Uso:**
- Registro de depuración
- Seguimiento del comportamiento del usuario
- Monitoreo de errores
- Métricas de rendimiento

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

**Funciones de optimización para móvil:**
- Posicionamiento en la parte inferior (de fácil acceso para el pulgar)
- Ancho basado en porcentaje (máximo 80%)
- Duración más corta (2 segundos)
- Objetivos de toque más grandes
- Sin superposición (sin bloquear)

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

### 2. Notificaciones no bloqueantes

Para una mejor experiencia de usuario, usa notificaciones estilo toast no bloqueantes en lugar de alertas modales:

```javascript
// ❌ Blocks user interaction
alert(`${title}: ${content}`);

// ✅ Non-blocking
showToastNotification(title, content);
```

### 3. Duración apropiada

Elige duraciones de autodescarte apropiadas según la longitud del contenido:

```javascript
const duration = content.length > 50 ? 5000 : 3000;
setTimeout(remove, duration);
```

### 4. Accesibilidad

Asegúrate de que tu toast personalizado sea accesible:

```javascript
toast.setAttribute('role', 'alert');
toast.setAttribute('aria-live', 'polite');
toast.setAttribute('aria-atomic', 'true');
```

### 5. Manejo de errores

Envuelve tu función de toast en try-catch para evitar que rompa la hoja de cálculo:

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

### 6. Limpieza de recursos

Siempre elimina los elementos DOM y los oyentes de eventos:

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

### 7. Restaurar por defecto cuando sea necesario

Proporciona una forma de restaurar el comportamiento predeterminado del toast:

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

### Fugas de memoria

**Problema:** La página se vuelve lenta después de muchas notificaciones toast.

**Solución:** Limpiar los elementos DOM y los escuchadores de eventos:
```javascript
const remove = () => {
  document.body.removeChild(toast);
  toast.onclick = null;  // Remove event listeners
  if (callback) callback();
};
```

### Problemas de Pantalla en Móviles

**Problema:** La notificación (Toast) se ve mal en dispositivos móviles.

**Soluciones:**
1. Usa anchos en porcentaje: `maxWidth: '80%'`
2. Add viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
3. Usa tamaños de fuente relativos: `fontSize: '14px'` en lugar de píxeles fijos

---



