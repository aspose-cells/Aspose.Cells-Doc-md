---
title: GridJs de mesaj ipucu toast görünümünü nasıl özelleştirilir  
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/how-to-customize-toast/
description: Bu makale, GridJs de mesaj toast UI görünümünü nasıl özelleştireceğinizi anlatmaktadır.
keywords: GridJs, özelleştirilebilir, toast, UI, görünüm, görsel, mesaj, uyarı
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

# GridJs için Özel Toast Kılavuzu

## Genel Bakış

GridJs, varsayılan toast mesajlarını kendi bildirim uygulamanızla değiştirebileceğiniz esnek bir özelleştirilebilir toast bildirim sistemi sağlar. Bu kılavuz, uygulamanızın ihtiyaçlarına göre toast bildirimlerini nasıl özelleştireceğinizi gösterir.

## İçindekiler

- [Temel Kullanım](#basic-usage)
- [Entegrasyon Örnekleri](#integration-examples)
  - [Güzel Özelleştirilmiş Toast](#1-beautiful-custom-toast)
  - [Toastr Kütüphanesi](#2-toastr-library-integration)
  - [SweetAlert2](#3-sweetalert2-integration)
  - [Vue + Element UI](#4-vue--element-ui)
  - [React + Ant Design](#5-react--ant-design)
- [İleri Düzey Kullanım Durumları](#advanced-use-cases)
  - [Kayıt ve Analitik](#6-logging-and-analytics)
  - [Mobil Uyumlu Toast](#7-mobile-friendly-toast)
- [API Referansı](#api-reference)
- [En İyi Uygulamalar](#best-practices)

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

**Parametreler:**
- `title` (dize): Toast bildirim başlığı
- `content` (dize): Toast mesaj içeriği
- `callback` (fonksiyon, isteğe bağlı): Toast kapandıktan sonra çalıştırılacak geri arama fonksiyonu

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

**Özellikler:**
- Gradyan arka plan
- Modal örtüsü
- Tıkla kapat
- 3 saniye sonra otomatik kapa
- Kapatma düğmesi

---

### 2. Toastr Library Integration

Integrate the popular [Toastr](https://github.com/CodeSeven/toastr) library for toast notifications.

**Prerequisites:**
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
```

**Uygulama:**
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

** Özelleştirme Seçenekleri:**
- `closeButton`: Kapatma düğmesi gösterir
- `progressBar`: Geri sayım ilerleme çubuğu gösterir
- `positionClass`: Bildirim konumunu kontrol eder (üst-sağ, alt-sol vb.)
- `timeOut`: Otomatik kapanma süresi milisaniye cinsinden

---

### 3. SweetAlert2 Integration

Use [SweetAlert2](https://sweetalert2.github.io/) for beautiful, customizable alert dialogs.

**Prerequisites:**
```html
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
```

**Uygulama:**
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

**Mevcut Semboller:**
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

**Bildirim Türleri:**
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

**Alternatif Ant Tasarım Bileşenleri:**
- `message.success()`
- `message.error()`
- `message.warning()`
- `notification.open()` (daha karmaşık bildirimler için)

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

**Kullanım Durumları:**
- Hata ayıklama günlüğü
- Kullanıcı davranışı takibi
- Hata izleme
- Performans ölçümleri

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

**Mobil Optimizasyon Özellikleri:**
- Alt konumlandırma (başparmak dostu)
- Yüzde tabanlı genişlik (max 80%)
- Daha kısa süre (2 saniye)
- Daha büyük dokunma hedefleri
- Katman yok (bloklamayan)

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

### 2. Bloklamayan Bildirimler

Daha iyi kullanıcı deneyimi için, modal uyarılar yerine bloklamayan tost bildirimi kullanın:

```javascript
// ❌ Blocks user interaction
alert(`${title}: ${content}`);

// ✅ Non-blocking
showToastNotification(title, content);
```

### 3. Uygun Süre

İçerik uzunluğuna göre uygun otomatik kapama süreleri seçin:

```javascript
const duration = content.length > 50 ? 5000 : 3000;
setTimeout(remove, duration);
```

### 4. Erişilebilirlik

Özel tostunuzun erişilebilir olduğundan emin olun:

```javascript
toast.setAttribute('role', 'alert');
toast.setAttribute('aria-live', 'polite');
toast.setAttribute('aria-atomic', 'true');
```

### 5. Hata İşleme

Tabloyu bozmayacak şekilde toast fonksiyonunuzu try-catch ile sarmalayın:

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

### 6. Kaynakları Temizle

Her zaman DOM öğelerini ve olay dinleyicilerini temizleyin:

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

### 7. Gerektiğinde Varsayılanı Geri Yükle

Varsayılan toast davranışını geri yükleme yolu sağlayın:

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

### Bellek Sızıntıları

**Sorun:** Sayfa birçok toast bildirimi sonrası yavaşlar.

**Çözüm:** DOM öğelerini ve olay dinleyicilerini temizleyin:
```javascript
const remove = () => {
  document.body.removeChild(toast);
  toast.onclick = null;  // Remove event listeners
  if (callback) callback();
};
```

### Mobil Görüntüleme Sorunları

**Sorun:** Toast mobil cihazlarda kötü görünür.

**Çözümler:**
1. Yüzde tabanlı genişlikler kullanın: `maxWidth: '80%'`
2. Add viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
3. Oransal font boyutları kullanın: `fontSize: '14px'` yerine sabit piksel kullanın

---



