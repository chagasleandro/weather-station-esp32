# 🌤️ Estação Meteorológica com ESP32 e MicroPython

Este projeto é uma estação meteorológica simples com ESP32, escrita em Python (MicroPython), que mede temperatura e umidade e publica os dados via MQTT para visualização em tempo real com Grafana.

## 🔧 Tecnologias
- ESP32 + MicroPython
- Sensor DHT11 ou DHT22
- MQTT (Broker Mosquitto)
- Grafana + InfluxDB (opcional)
- Python

## ⚙️ Funcionalidades
- Conecta ao Wi-Fi
- Lê dados de temperatura e umidade
- Publica em tópicos MQTT
- Integra com dashboards

## 📦 Estrutura

---

## 🔌 Esquema de Ligação

- Sensor DHT22:
  - VCC → 3V3 do ESP32
  - DATA → GPIO4 do ESP32 (com resistor de 10kΩ entre DATA e VCC)
  - GND → GND do ESP32

📷 Ver esquema: ![Image](https://github.com/user-attachments/assets/1dce724d-c03a-4f2b-bb19-1080df098bc5)
---

## 📡 Tópicos MQTT

- `estacao/temperatura`
- `estacao/umidade`

---

## 🛠️ Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/chagasleandro/weather-station-esp32.git

📸 Imagens do Projeto

Imagens reais da montagem do projeto: ![Image](https://github.com/user-attachments/assets/a1a1e07a-9bda-4186-ae1a-adf00bc9b00d)

✨ Melhorias Futuras

    Adicionar sensores extras (pressão, luminosidade, etc)

    Web interface para configuração

    Gravação de dados em SD ou banco local

    Integração com Node-RED

🤝 Contribuindo

Pull requests são bem-vindos! Para mudanças maiores, abra uma issue antes para discutir o que você gostaria de modificar.
👨‍💻 Autor

Desenvolvido por Leandro Chagas
📧 leandrosrs2012@gmail.com
🔗 GitHub | LinkedIn
📝 Licença

Este projeto está sob a licença MIT.
