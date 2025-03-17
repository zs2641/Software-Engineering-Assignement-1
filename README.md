# Software-Engineering-Assignment-1

## UC 1.01

**Name und Identifikationsnummer:** UC 1.01.-Proband:in anlegen  
**Beschreibung:** es werden verschiedene Proband:in angelegt  
**Beteiligte Akteure:** Diagnostiker:in, Proband:in   
**Status:** in Arbeit  
**Auslöser:** Durchführung einer standartisierten Leistungsdiagnostik  
**Vorbedingung:** keine  
**Invariante:** Aufzeichnung der bis zum Abbruch erhobenen Daten  
**Nachbedingung/Ergebnis:** UC 1.01. Proband:innen wurden angelegt  
**Standardablauf:** Alle Daten der Proband:innen werden angelegt und gespeichert  
**Änderungsgeschichte:** 0.01; 15.03.2025.; Sophia Österle  

## UC 1.03
**Name und Identifikationsnummer:** UC 1.03 - Warnung bei Maximalpulsüberschreitung oder Leistungsabweichung

**Beschreibung:** Eine Warnung wird angezeigt, wenn der Maximalpuls überschritten oder die vorgegebene Leistung abweicht, damit der Test abgebrochen werden kann.

**Beteiligte Akteure:** Diagnostiker:in

**Status:** in Arbeit

**Auslöser:** Überschreiten des Maximalpulses oder Abweichung von der vorgegebenen Leistung

**Vorbedingung:** Der Test läuft, und relevante Daten (Puls, Leistung) werden erfasst

**Invariante:** Die Warnung wird unabhängig von anderen Faktoren ausgelöst, wenn eine Abweichung erkannt wird

**Nachbedingung/Ergebnis:** Der Diagnostiker/die Diagnostikerin wurde über die Abweichung informiert und kann den Test abbrechen

**Standardablauf: Das System überwacht kontinuierlich die Puls- und Leistungswerte.

Sobald eine Abweichung erkannt wird (Maximalpuls überschritten oder Leistungsabweichung), wird eine Warnung generiert.

Die Warnung wird auf dem Bildschirm des Diagnostikers/der Diagnostikerin angezeigt.

**Änderungsgeschichte:** 0.01; 17.03.2025; Sophie Zembacher


