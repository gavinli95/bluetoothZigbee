clc;
close all;
clearvars;

matname = "data/52.mat";
[y, Fs] = audioread("okgooglepred.wav");
t = length(y)/Fs;


root = "/dev/cu."
master_port = root + "usbmodem0011";
slave_ports = root + ["usbmodem2", "usbmodem3", "usbmodem4", "usbmodem5", "usbmodem6", "usbmodem7", "usbmodem8", "usbmodem9", "usbmodem10", "usbmodem11", "usbmodem12", "usbmodem13", "usbmodem14", "usbmodem15", "usbmodem16", "usbmodem17"];

master = serialport(master_port, 115200);

slaves = [];
for i = 1:16
    slave = serialport(slave_ports(i), 115200);
    slaves = [slaves slave];
end

sound(y, Fs);
pause(0.43333);
write(master, "12345", "uint8");
pause(1.6);

tic;

datas = [];
for i = 1:16
    data = []
    for j = 1:16
        write(slaves(i), "send", "uint8");
        data = [data read(slaves(i), 100, "uint8")];
        if length(data) == 0
            delete(master);
            delete(slaves);
            return;
        end
    end

    %temp_data = [];
    %for j = 0:159
    %    temp = data(j * 10 + 1 : j* 10 + 10);
    %    temp_data = [temp_data max(temp)];
    %end

    datas = [datas ; data];
    pause(1);
end

time = toc;

delete(master);
delete(slaves);

data = -datas;

save(matname, "data");

clc;
close all;
clearvars;

%average_noise = mean(datas);

%figure;
%h = heatmap(data, 'CellLabelColor', 'none', 'MissingDataColor', 'white', 'ColorLimits', [-110, -50]);
%h = heatmap(data, 'CellLabelColor', 'none', 'MissingDataColor', 'white');

%h.GridVisible = 'off';

%col = [62];
%xline(ax, [col-.1, col+.1], 'k-', 'Alpha', 1);

%labels = [];
%for i = 1:1600
%    labels = [labels ""];
%end
%h.XDisplayLabels = labels;
%saveas(h, "music.png", "png");

