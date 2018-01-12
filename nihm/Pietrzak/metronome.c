#include <gpio.h>
#include <timer.h>
#include <stdio.h>

static volatile int freq;
static volatile int statusButton = 0;


void toggleled(){
   statusButton ^=1;
}

void update(){
    if(freq == 0)
	freq = 440;
    else
        freq = 0;
}


int main() {
    //Initialize the pin_t structure with the pin port and number
    //On this board there is a LED on PA7
    pin_t pin = make_pin(gpio_port_a, 7);
    pin_t buz = make_pin(gpio_port_a, 2);
    pin_t button = make_pin(gpio_port_a, 6);
    timer_channel_t tc1, tc2;
    int statut=1;
   // uint8_t roue;

    //configure pin for output.
    gpio_config(pin, pin_dir_write, pull_down);
    gpio_config(buz, pin_dir_write, pull_down);

    // configure pin for input
    gpio_config(button, pin_dir_read, pull_down);

    //attach the callback to the rising trigger on this pin
    gpio_irq_init(button, toggleled, rising);


    //configure timer for led
    tc1.channel = 2;
    tc1.timer = 3;
    timer_config(tc1.timer, 18000,6000);
    timer_pwmchannel_init(tc1, pin, 0);
    //configure timer for buzzer
    tc2.channel = 3;
    tc2.timer = 5;
    timer_config(tc2.timer, 18000,6000);
    timer_irq_init(tc2, event_update, update);


 

    while(1){
        gpio_set(buz, freq);
        gpio_set(pin, statut);
	if(statusButton){
		timer_pwmchannel_init(tc1, pin, 12);
		if(statut)
		  statut--;
 		else
		  statut++;
       }else{
		timer_pwmchannel_init(tc1, pin, 0);
      }
   }
   return 0;
}
