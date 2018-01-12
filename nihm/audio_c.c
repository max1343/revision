// Q1.1 
// Il existe deux façon de faire clignoter une led :
//  - Avec un sleep ;
//  - Avec un timer.

// Q1.2
// Pour le sleep : 
//  - L'avantage est que cette solution est simple à mettre en place ;
//  - L'incovenient est que l'appel à cette fonction est bloquante.
// Pour le timer :
//  - L'avantage est que l'appel à cette fonction n'est pas bloquante ;
//  - L'inconvenient est que cette solution est plus complexe à mettre en oeuvre, notamment à cause du calcul du (prescale, count).


// Question 1.3 et 1.4
#define FREQ 44000       // Hz
#define RECORDING_TIME 2 // sec
uint16_t data[FREQ * RECORDING_TIME];

// Q1.3 - Enregistrement 
pin_t micro_pin;

void record(void)
{
    static unsigned pos = 0;
    data[pos++] = adc_get(micro_pin);
}

int main(void) 
{
    adc_t adc         = /* Choisir un adc */;
    channel_t channel = /* Choisir un channel pour l'ADC */;

    micro_pin = make_pin(/* Choisir un pin (2 param) */);
    
    adc_config_single(adc, channel, micro_pin); // Configuer l'ADC

    timer_channel_t tchannel = /* Init tchannel */;
    uint16_t prescale = /* Determiner le bon prescale */;
    uint32_t count    = /* Determiner le bon count */;
    timer_config(tchannel.timer, prescale, count);
    timer_irq_init(timer, event_update, record);

    for (;;);

    return 0;
}

// Q1.4 - Lecture
dac_t speaker_pin;
void play(void)
{
    static unsigned pos = 0;
    dac_set(speaker_pin, data[pos++]);
}

int main(void)
{
    dac_t dac = /* Choisir un dac */;
    speaker_pin = make_pin(/* Choisir un pin */);
    
    dac_port_t dac_port = {speaker_pin, dac}
    dac_config(dac_port);

    timer_channel_t tchannel = /* Init tchannel */;
    uint16_t prescale = /* Determiner le bon prescale */;
    uint32_t count    = /* Determiner le bon count */;
    timer_config(tchannel.timer, prescale, count);
    timer_irq_init(timer, event_update, play);

    for (;;);

    return 0;
}